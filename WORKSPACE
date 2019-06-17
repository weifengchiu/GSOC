# Copyright 2018 The TensorFlow Hub Authors. All Rights Reserved.
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
# ==============================================================================
workspace(name = "gsoc")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

git_repository(
    name = "org_tensorflow_hub",
    commit = "eeefe60480d8471b1662259f8eb5a965eba13d18",
    remote = "https://github.com/tensorflow/hub.git",
)

bind(
    name = "tensorflow_hub",
    actual = "@org_tensorflow_hub//tensorflow_hub:tensorflow_hub"
)
bind(
    name = "expect_tensorflow_installed",
    actual = "@org_tensorflow_hub//tensorflow_hub:expect_tensorflow_installed"
)
bind(
    name = "expect_numpy_installed",
    actual = "@org_tensorflow_hub//tensorflow_hub:expect_numpy_installed"
)
git_repository(
    name = "protobuf_bzl",
    # v3.6.1.3
    commit = "66dc42d891a4fc8e9190c524fd67961688a37bbe",
    remote = "https://github.com/google/protobuf.git",
)
bind(
    name = "protobuf",
    actual = "@protobuf_bzl//:protobuf",
)
bind(
    name = "protobuf_python",
    actual = "@protobuf_bzl//:protobuf_python",
)
bind(
    name = "protobuf_python_genproto",
    actual = "@protobuf_bzl//:protobuf_python_genproto",
)
bind(
    name = "protoc",
    actual = "@protobuf_bzl//:protoc",
)
# Using protobuf version 3.6.1.3
http_archive(
    name = "com_google_protobuf",
    strip_prefix = "protobuf-3.6.1.3",
    urls = ["https://github.com/google/protobuf/archive/v3.6.1.3.zip"],
)

# required by protobuf_python
http_archive(
    name = "six_archive",
    build_file = "@protobuf_bzl//:six.BUILD",
    sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a",
    url = "https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz#md5=34eed507548117b2ab523ab14b2f8b55",
)
bind(
    name = "six",
    actual = "@six_archive//:six",
)
