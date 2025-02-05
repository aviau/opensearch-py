# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#
#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.


from opensearchpy.exceptions import TransportError

from .test_cases import TestCase


class TestTransformError(TestCase):
    def test_transform_error_parse_with_error_reason(self) -> None:
        e = TransportError(
            500,
            "InternalServerError",
            {"error": {"root_cause": [{"type": "error", "reason": "error reason"}]}},
        )

        self.assertEqual(
            str(e), "TransportError(500, 'InternalServerError', 'error reason')"
        )

    def test_transform_error_parse_with_error_string(self) -> None:
        e = TransportError(
            500, "InternalServerError", {"error": "something error message"}
        )

        self.assertEqual(
            str(e),
            "TransportError(500, 'InternalServerError', 'something error message')",
        )
