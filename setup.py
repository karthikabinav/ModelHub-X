# Copyright 2021 The HuggingFace Team. All rights reserved.
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

from setuptools import find_packages, setup

extras = {}
extras["quality"] = ["ruff == 0.13.1"]
extras["docs"] = []
extras["test_prod"] = ["pytest>=7.2.0", "pytest-xdist", "pytest-subtests", "parameterized", "pytest-order"]
extras["testing"] = extras["test_prod"]
setup(name="accelerate", version="1.16.0.dev0", description="Accelerate", license="Apache", author="The Hugging Face team", url="https://github.com/huggingface/accelerate", package_dir={"": "src"}, packages=find_packages("src"), python_requires=">=3.10.0", install_requires=["numpy>=1.17", "packaging>=20.0", "psutil", "pyyaml", "torch>=2.0.0", "huggingface_hub>=0.21.0", "safetensors>=0.4.3"], extras_require=extras)
