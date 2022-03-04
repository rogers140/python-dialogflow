# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for SuggestArticles
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_generated_dialogflow_v2beta1_Participants_SuggestArticles_async]
from google.cloud import dialogflow_v2beta1


async def sample_suggest_articles():
    # Create a client
    client = dialogflow_v2beta1.ParticipantsAsyncClient()

    # Initialize request argument(s)
    request = dialogflow_v2beta1.SuggestArticlesRequest(
        parent="parent_value",
    )

    # Make the request
    response = await client.suggest_articles(request=request)

    # Handle the response
    print(response)

# [END dialogflow_generated_dialogflow_v2beta1_Participants_SuggestArticles_async]