# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Error message helper for TFDS."""

import contextlib
import dataclasses
from typing import Callable, Iterator, List, Type, Union

from etils import edc
from tensorflow_datasets.core import utils

Message = Union[str, Callable[[], str]]


@dataclasses.dataclass
class ErrorContext:
  """Stack container for error context.

  This stack keeps track of the error messages which are raised when loading a
  dataset. These error messages are used to provide better context for the users
  in case of DatasetNotFound errors are raised.
  """

  messages: List[Message] = dataclasses.field(default_factory=list)


# Current error context. Accessed by `reraise_with_context` and `add_context`.
@edc.dataclass
@dataclasses.dataclass
class ContextHolder:
  # Each thread will use its own instance of current_context_msg.
  current_context_msg: edc.ContextVar[ErrorContext | None] = None


context_holder = ContextHolder()


@contextlib.contextmanager
def record_error_context() -> Iterator[ErrorContext]:
  """Contextmanager which captures the error context for a thread."""

  if context_holder.current_context_msg is not None:
    raise ValueError(
        'Cannot record error context within the scope of another error context.'
    )

  context_holder.current_context_msg = ErrorContext()
  try:
    yield context_holder.current_context_msg
  finally:
    context_holder.current_context_msg = None


@contextlib.contextmanager
def reraise_with_context(error_cls: Type[Exception]) -> Iterator[None]:
  """Contextmanager which reraises an exception with an additional message.

  Args:
    error_cls: The exception to be reraised.

  Yields:
    None.
  """
  # If current_context_msg exists, we are already within the scope of the
  # session contextmanager.
  if context_holder.current_context_msg is not None:
    yield
    return

  context_holder.current_context_msg = ErrorContext()
  try:
    yield
  except error_cls as e:
    context_msg = '\n'.join(context_holder.current_context_msg.messages)
    utils.reraise(e, suffix=context_msg)
  finally:
    context_holder.current_context_msg = None


def add_context(msg: str) -> None:
  """Appends the error message to the error context stack.

  Args:
    msg: The error message to add to the error context stack.

  Returns:
    None.

  Raises:
    AttributeError if local thread has no current_context_msg attribute.
  """
  if context_holder.current_context_msg is None:
    raise AttributeError(
        'add_context called outside of reraise_with_context contextmanager.'
    )
  context_holder.current_context_msg.messages.append(msg)
