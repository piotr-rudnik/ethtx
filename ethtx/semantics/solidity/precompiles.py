#  Copyright 2021 DAI Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from ethtx.models.semantics_model import FunctionSemantics, ParameterSemantics

precompiles = {
    1: FunctionSemantics(
        signature="",
        name="ecrecover",
        inputs=[
            ParameterSemantics(name="hash", type="bytes32"),
            ParameterSemantics(name="v", type="bytes8"),
            ParameterSemantics(name="r", type="bytes32"),
            ParameterSemantics(name="s", type="bytes32"),
        ],
        outputs=[ParameterSemantics(name="", type="address")],
    ),
    2: FunctionSemantics(
        signature="",
        name="sha256",
        inputs=[ParameterSemantics(name="data", type="raw")],
        outputs=[ParameterSemantics(name="", type="bytes32")],
    ),
    3: FunctionSemantics(
        signature="",
        name="ripemd160",
        inputs=[ParameterSemantics(name="data", type="raw")],
        outputs=[ParameterSemantics(name="", type="bytes32")],
    ),
    4: FunctionSemantics(
        signature="",
        name="datacopy",
        inputs=[ParameterSemantics(name="data", type="raw")],
        outputs=[ParameterSemantics(name="", type="raw")],
    ),
    5: FunctionSemantics(
        signature="",
        name="bigModExp",
        inputs=[
            ParameterSemantics(name="base", type="bytes32"),
            ParameterSemantics(name="exp", type="bytes32"),
            ParameterSemantics(name="mod", type="bytes32"),
        ],
        outputs=[ParameterSemantics(name="", type="bytes32")],
    ),
    6: FunctionSemantics(
        signature="",
        name="bn256Add",
        inputs=[
            ParameterSemantics(name="ax", type="bytes32"),
            ParameterSemantics(name="ay", type="bytes32"),
            ParameterSemantics(name="bx", type="bytes32"),
            ParameterSemantics(name="by", type="bytes32"),
        ],
        outputs=[ParameterSemantics(name="", type="bytes32[2]")],
    ),
    7: FunctionSemantics(
        signature="",
        name="bn256ScalarMul",
        inputs=[
            ParameterSemantics(name="x", type="bytes32"),
            ParameterSemantics(name="y", type="bytes32"),
            ParameterSemantics(name="scalar", type="bytes32"),
        ],
        outputs=[ParameterSemantics(name="", type="bytes32[2]")],
    ),
    8: FunctionSemantics(
        signature="",
        name="bn256Pairing",
        inputs=[ParameterSemantics(name="input", type="raw")],
        outputs=[ParameterSemantics(name="", type="bytes32")],
    ),
}
