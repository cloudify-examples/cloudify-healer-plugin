############
# Copyright (c) 2019 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############


def test_doping():
    from cloudify_healer.healer import doPing

    res = doPing("8.8.8.8")
    assert not res


def test_basic_dohttp():
    from cloudify_healer.healer import doHttp

    nodeconfig = {}
    nodeconfig['config'] = {}
    res = doHttp("http://cloudify.co", 1, nodeconfig)
    assert not res


def test_dosocket():
    from cloudify_healer.healer import doSocket

    nodeconfig = {}
    nodeconfig['config'] = {}
    nodeconfig['config']['port'] = 22

    res = doSocket("127.0.0.1", nodeconfig)
    assert not res
