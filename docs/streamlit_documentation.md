### Quick Start: Initialize Client, Send Message, and Log Response (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/overview

This quick start example provides a complete, runnable snippet for getting started with the OpenRouter TypeScript SDK. It covers initializing the client, sending a basic chat message to an AI model, and then logging the content of the model's response to the console.

```typescript
import OpenRouter from '@openrouter/sdk';

const client = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY
});

const response = await client.chat.send({
  model: "minimax/minimax-m2",
  messages: [
    { role: "user", content: "Hello!" }
  ]
});

console.log(response.choices[0].message.content);
```

--------------------------------

### Install OpenRouter SDK via npm

Source: https://openrouter.ai/docs/index

Install the official OpenRouter SDK package using npm package manager. This is the first step to use the OpenRouter SDK in your project.

```bash
npm install @openrouter/sdk
```

--------------------------------

### Install OpenRouter SDK with npm, yarn, or pnpm

Source: https://openrouter.ai/docs/quickstart

Install the OpenRouter SDK package using your preferred Node.js package manager. Supports npm, yarn, and pnpm installation methods.

```bash
npm install @openrouter/sdk
```

```bash
yarn add @openrouter/sdk
```

```bash
pnpm add @openrouter/sdk
```

--------------------------------

### Quick Start: Basic Chat Completion

Source: https://openrouter.ai/docs/sdks/python/overview

Quick start example demonstrating basic chat completion with OpenRouter SDK. Shows initialization, sending a message, and retrieving the response content.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY")
) as client:
    response = client.chat.send(
        model="minimax/minimax-m2",
        messages=[
            {"role": "user", "content": "Hello!"}
        ]
    )

    print(response.choices[0].message.content)
```

--------------------------------

### OpenRouter SDK Initialization

Source: https://openrouter.ai/docs/index

Initialize the OpenRouter SDK with your API key and optional headers for app attribution. The SDK provides a TypeScript-first interface for interacting with OpenRouter's unified API.

```APIDOC
## SDK Initialization

### Description
Initialize the OpenRouter SDK with authentication credentials and optional app attribution headers. This setup enables you to make API requests with automatic error handling and type safety.

### Installation
```
npm install @openrouter/sdk
```

### Configuration Parameters
- **apiKey** (string) - Required - Your OpenRouter API key
- **defaultHeaders** (object) - Optional - Default headers for all requests
  - **HTTP-Referer** (string) - Optional - Your site URL for rankings
  - **X-Title** (string) - Optional - Your site name for rankings

### Initialization Example
```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': '<YOUR_SITE_URL>',
    'X-Title': '<YOUR_SITE_NAME>'
  }
});
```

### Usage Example
```typescript
const completion = await openRouter.chat.send({
  model: 'openai/gpt-5.2',
  messages: [
    {
      role: 'user',
      content: 'What is the meaning of life?'
    }
  ],
  stream: false
});

console.log(completion.choices[0].message.content);
```
```

--------------------------------

### Configure OpenClaw using the setup wizard (Bash)

Source: https://openrouter.ai/docs/guides/guides/openclaw-integration

This command launches an interactive setup wizard that guides users through integrating OpenClaw with OpenRouter. It simplifies the process of choosing OpenRouter as a provider, entering an API key, selecting a model, and configuring messaging channels.

```bash
openclaw onboard
```

--------------------------------

### Install Dependencies for Skills System

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

Install required packages for the skills loader implementation. Requires the OpenRouter SDK and Zod for schema validation.

```bash
pnpm add @openrouter/sdk zod
```

--------------------------------

### Initialize OpenRouter SDK and send chat completion

Source: https://openrouter.ai/docs/index

Create an OpenRouter client instance with API key and optional headers for app attribution, then send a chat completion request. The SDK handles model selection and fallbacks automatically.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
    'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
  },
});

const completion = await openRouter.chat.send({
  model: 'openai/gpt-5.2',
  messages: [
    {
      role: 'user',
      content: 'What is the meaning of life?',
    },
  ],
  stream: false,
});

console.log(completion.choices[0].message.content);
```

--------------------------------

### Guide OpenRouter Model Response with Assistant Prefill (TypeScript)

Source: https://openrouter.ai/docs/api-reference/overview

This TypeScript code illustrates how to use OpenRouter's assistant prefill feature to guide a model's response. By appending a message with `role: 'assistant'` and a partial `content` string to the `messages` array, you can prompt the model to complete a specific phrase or structure. This technique is useful for steering the model towards desired output formats or starting points.

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    Authorization: 'Bearer <OPENROUTER_API_KEY>',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    model: 'openai/gpt-5.2',
    messages: [
      { role: 'user', content: 'What is the meaning of life?' },
      { role: 'assistant', content: "I'm not sure, but my best guess is" }
    ]
  })
});
```

--------------------------------

### Initialize OpenRouter SDK and send chat completion in TypeScript

Source: https://openrouter.ai/docs/quickstart

Create an OpenRouter client instance with API key and optional headers for app attribution, then send a chat completion request. Returns the model's response content.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': '<YOUR_SITE_URL>',
    'X-Title': '<YOUR_SITE_NAME>',
  },
});

const completion = await openRouter.chat.send({
  model: 'openai/gpt-5.2',
  messages: [
    {
      role: 'user',
      content: 'What is the meaning of life?',
    },
  ],
  stream: false,
});

console.log(completion.choices[0].message.content);
```

--------------------------------

### Make an API Request with an OpenRouter Preset (Quick Start)

Source: https://openrouter.ai/docs/guides/features/presets

This example demonstrates how to quickly make an OpenRouter API request by referencing a preset directly in the 'model' field. This method abstracts away complex configurations, allowing the application to simply call a named preset.

```json
{
  "model": "@preset/ravenel-bridge",
  "messages": [
    {
      "role": "user",
      "content": "What's your opinion of the Golden Gate Bridge? Isn't it beautiful?"
    }
  ]
}
```

--------------------------------

### Demonstrate Interactive OpenRouter AI MCP Client Usage in Bash

Source: https://openrouter.ai/docs/guides/guides/mcp-servers

This Bash example illustrates how to run the `mcp-client.py` script, showcasing its interactive chat loop. It demonstrates the client connecting to a server, identifying available tools, and processing user queries by invoking tools like `list_allowed_directories` and `search_files` to answer questions about installed applications.

```bash
% python mcp-client.py

Secure MCP Filesystem Server running on stdio
Allowed directories: [ '/Applications' ]

Connected to server with tools: ['read_file', 'read_multiple_files', 'write_file'...]

MCP Client Started!
Type your queries or 'quit' to exit.

Query: Do I have microsoft office installed?

Result:
[Calling tool list_allowed_directories with args {}]
I can check if Microsoft Office is installed in the Applications folder:

Query: continue

Result:
[Calling tool search_files with args {'path': '/Applications', 'pattern': 'Microsoft'}]
Now let me check specifically for Microsoft Office applications:

Query: continue

Result:
I can see from the search results that Microsoft Office is indeed installed on your system.
The search found the following main Microsoft Office applications:

1. Microsoft Excel - /Applications/Microsoft Excel.app
2. Microsoft PowerPoint - /Applications/Microsoft PowerPoint.app
3. Microsoft Word - /Applications/Microsoft Word.app
4. OneDrive - /Applications/OneDrive.app (which includes Microsoft SharePoint integration)
```

--------------------------------

### Install Dependencies for Weather Tool

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/weather-tool

Install required packages for the weather tool implementation. Requires @openrouter/sdk for API integration and zod for schema validation. Additionally, set up environment variables for WeatherAPI and OpenRouter API keys.

```bash
pnpm add @openrouter/sdk zod
```

```bash
export WEATHER_API_KEY=your_api_key_here
export OPENROUTER_API_KEY=your_openrouter_key
```

--------------------------------

### Basic OpenRouter integration with Mastra Agent

Source: https://openrouter.ai/docs/community/mastra

Complete example demonstrating how to initialize OpenRouter provider, create a Mastra Agent with OpenRouter model, and generate responses from user messages. Shows the full workflow from setup to response generation.

```typescript
import { Agent } from '@mastra/core/agent';
import { createOpenRouter } from '@openrouter/ai-sdk-provider';

// Initialize the OpenRouter provider
const openrouter = createOpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

// Create an agent using OpenRouter
const assistant = new Agent({
  model: openrouter('anthropic/claude-3-opus'),
  name: 'Assistant',
  instructions: 'You are a helpful assistant.',
});

// Generate a response
const response = await assistant.generate([
  {
    role: 'user',
    content: 'Tell me about renewable energy sources.',
  },
]);

console.log(response.text);
```

--------------------------------

### Integrate with OpenRouter AI using OpenAI SDK (TypeScript/Python)

Source: https://openrouter.ai/docs/quickstart

This snippet demonstrates how to configure and use the OpenAI SDK to interact with the OpenRouter AI API. It shows how to set the `baseURL` (or `base_url`), `apiKey`, and optional `HTTP-Referer` and `X-Title` headers for site identification and ranking on OpenRouter.ai. A basic chat completion request is included to illustrate API usage.

```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://openrouter.ai/api/v1',
  apiKey: '<OPENROUTER_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
    'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
  },
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: 'openai/gpt-5.2',
    messages: [
      {
        role: 'user',
        content: 'What is the meaning of life?',
      },
    ],
  });

  console.log(completion.choices[0].message);
}

main();
```

```python
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  model="openai/gpt-5.2",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)

print(completion.choices[0].message.content)
```

--------------------------------

### GET Activity API with Bearer Authentication - Multi-Language

Source: https://openrouter.ai/docs/api/api-reference/analytics/get-user-activity

Demonstrates how to make an authenticated GET request to the OpenRouter AI activity endpoint across multiple programming languages. Each example includes proper header setup with Bearer token authentication and response handling. Requires a valid OpenRouter API token and internet connectivity.

```python
import requests

url = "https://openrouter.ai/api/v1/activity"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/activity';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/activity"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/activity")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/activity")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/activity', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/activity");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/activity")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Update Guardrail - Ruby Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail

Ruby implementation using the Net::HTTP library to update a guardrail. Shows proper SSL configuration and request setup for Ruby applications.

```APIDOC
### Ruby Implementation

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Updated Guardrail Name\",\n  \"description\": \"Updated description\",\n  \"limit_usd\": 75,\n  \"reset_interval\": \"weekly\"\n}"

response = http.request(request)
puts response.read_body
```

**Usage Notes:**
- Replace `<token>` with your actual Bearer token
- Set `use_ssl = true` for HTTPS connections
- Use `Net::HTTP::Patch` for PATCH requests
- Call `read_body` to get the response content
```

--------------------------------

### OpenAI SDK Compatibility

Source: https://openrouter.ai/docs/index

Use OpenRouter with the OpenAI SDK by configuring the base URL to point to OpenRouter's API endpoint. This provides full compatibility with existing OpenAI SDK code.

```APIDOC
## OpenAI SDK Configuration

### Description
Configure the OpenAI SDK to use OpenRouter as the API provider by setting a custom base URL. This allows you to use OpenRouter's model access with familiar OpenAI SDK syntax.

### Configuration Parameters
- **baseURL** (string) - Required - Set to 'https://openrouter.ai/api/v1'
- **apiKey** (string) - Required - Your OpenRouter API key
- **defaultHeaders** (object) - Optional - Default headers for all requests
  - **HTTP-Referer** (string) - Optional - Your site URL for rankings
  - **X-Title** (string) - Optional - Your site name for rankings

### Setup Example
```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://openrouter.ai/api/v1',
  apiKey: '<OPENROUTER_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': '<YOUR_SITE_URL>',
    'X-Title': '<YOUR_SITE_NAME>'
  }
});
```

### Usage Example
```typescript
async function main() {
  const completion = await openai.chat.completions.create({
    model: 'openai/gpt-5.2',
    messages: [
      {
        role: 'user',
        content: 'What is the meaning of life?'
      }
    ]
  });

  console.log(completion.choices[0].message);
}

main();
```

### Features
- Full OpenAI SDK compatibility
- Streaming support
- Automatic model fallback handling
- Cost optimization across hundreds of models
```

--------------------------------

### POST /api/v1/chat/completions

Source: https://openrouter.ai/docs/quickstart

Sends a chat message to the OpenRouter API to get a model completion. This endpoint allows access to hundreds of AI models through a unified interface, supporting various AI models and handling optional attribution headers.

```APIDOC
## POST /api/v1/chat/completions

### Description
Sends a chat message to the OpenRouter API to get a model completion. This endpoint allows access to hundreds of AI models through a unified interface, supporting various AI models and handling optional attribution headers.

### Method
POST

### Endpoint
https://openrouter.ai/api/v1/chat/completions

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
- **model** (string) - Optional - The AI model to use for the completion (e.g., "openai/gpt-5.2").
- **messages** (array of objects) - Required - A list of message objects comprising the conversation history.
    - **messages[].role** (string) - Required - The role of the author of this message (e.g., "user", "assistant").
    - **messages[].content** (string) - Required - The content of the message.
- **stream** (boolean) - Optional - If true, the API will stream back partial message deltas. Default is false.

### Headers
- **Authorization** (string) - Required - Bearer token for authentication: `Bearer <OPENROUTER_API_KEY>`.
- **HTTP-Referer** (string) - Optional - Site URL for rankings on openrouter.ai.
- **X-Title** (string) - Optional - Site title for rankings on openrouter.ai.
- **Content-Type** (string) - Required - Must be `application/json`.

### Request Example
```json
{
  "model": "openai/gpt-5.2",
  "messages": [
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
}
```

### Response
#### Success Response (200)
- **id** (string) - A unique identifier for the chat completion.
- **object** (string) - The object type, which is always `chat.completion`.
- **created** (integer) - The Unix timestamp (in seconds) of when the chat completion was created.
- **model** (string) - The model used for the chat completion.
- **choices** (array of objects) - A list of chat completion choices.
    - **choices[].index** (integer) - The index of the choice in the list.
    - **choices[].message** (object) - A chat completion message generated by the model.
        - **choices[].message.role** (string) - The role of the author of this message, which is always `assistant`.
        - **choices[].message.content** (string) - The content of the message.
    - **choices[].finish_reason** (string) - The reason the model stopped generating tokens (e.g., "stop", "length").
- **usage** (object) - Usage statistics for the completion request.
    - **usage.prompt_tokens** (integer) - Number of tokens in the prompt.
    - **usage.completion_tokens** (integer) - Number of tokens in the generated completion.
    - **usage.total_tokens** (integer) - Total number of tokens used in the request (prompt + completion).

#### Response Example
```json
{
  "id": "chatcmpl-xxxxxxxxxxxxxxxxxxxxx",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "openai/gpt-5.2",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The meaning of life is a philosophical and existential question that has been pondered by humans throughout history. There is no single, universally accepted answer, and its interpretation often depends on individual beliefs, cultural contexts, and personal experiences."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 60,
    "total_tokens": 72
  }
}
```
```

--------------------------------

### Update Guardrail - Python Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail

Python implementation using the requests library to update a guardrail configuration. Demonstrates proper header setup and JSON payload formatting for the PATCH request.

```APIDOC
### Python Implementation

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000"

payload = {
    "name": "Updated Guardrail Name",
    "description": "Updated description",
    "limit_usd": 75,
    "reset_interval": "weekly"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

**Usage Notes:**
- Replace `<token>` with your actual Bearer token
- Replace the guardrail ID in the URL with your target guardrail
- The `requests.patch()` method automatically handles JSON serialization
- Check `response.status_code` for error handling
```

--------------------------------

### TraceQL Query Examples

Source: https://openrouter.ai/docs/guides/features/broadcast/grafana

Examples of common TraceQL queries to filter and analyze OpenRouter traces in Grafana Cloud.

```APIDOC
## TRACEQL Query Examples

### Description
This section provides various examples of TraceQL queries that can be used within Grafana Cloud's Explore feature to filter and analyze OpenRouter traces. These queries demonstrate how to select traces based on service name, duration, user ID, error status, and model used, as well as custom metadata.

### Method
QUERY

### Endpoint
N/A (Executed within Grafana Cloud's TraceQL interface)

### Parameters
#### Path Parameters
N/A

#### Query Parameters
N/A

#### Request Body
N/A

### Request Example
```traceql
{ resource.service.name = "openrouter" }
```

### Response
#### Success Response (200)
- **traces** (array) - A list of traces matching the query criteria. Each trace contains spans with various attributes.

#### Response Example
```json
[
  {
    "traceID": "a1b2c3d4e5f6g7h8",
    "spans": [
      {
        "spanID": "i9j0k1l2m3n4o5p6",
        "operationName": "chat",
        "attributes": {
          "resource.service.name": "openrouter",
          "gen_ai.request.model": "openai/gpt-4-turbo",
          "gen_ai.usage.total_tokens": 150,
          "trace.metadata.environment": "production"
        }
      }
    ]
  }
]
```

### Example Queries

#### All OpenRouter traces
```traceql
{ resource.service.name = "openrouter" }
```

#### Filter by specific model
```traceql
{ resource.service.name = "openrouter" && span.gen_ai.request.model = "openai/gpt-4-turbo" }
```

#### Find slow requests (> 5 seconds)
```traceql
{ resource.service.name = "openrouter" && duration > 5s }
```

#### Find requests by user
```traceql
{ resource.service.name = "openrouter" && span.user.id = "user_abc123" }
```

#### Find errors
```traceql
{ resource.service.name = "openrouter" && status = error }
```

#### Find requests by model (regex)
```traceql
{ resource.service.name = "openrouter" && span.gen_ai.request.model =~ ".*gpt-4.*" }
```

#### Querying Custom Metadata
```traceql
{ resource.service.name = "openrouter" && span.trace.metadata.environment = "production" }
```
```traceql
{ resource.service.name = "openrouter" && span.trace.metadata.alert_id = "alert_789" }
```
```

--------------------------------

### Send chat completion request to OpenRouter API with TypeScript fetch

Source: https://openrouter.ai/docs/quickstart

Make a POST request to OpenRouter's chat completions endpoint using the native fetch API. Includes API authentication and optional app attribution headers.

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    Authorization: 'Bearer <OPENROUTER_API_KEY>',
    'HTTP-Referer': '<YOUR_SITE_URL>',
    'X-Title': '<YOUR_SITE_NAME>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'openai/gpt-5.2',
    messages: [
      {
        role: 'user',
        content: 'What is the meaning of life?',
      },
    ],
  }),
});
```

--------------------------------

### Provide Comprehensive Descriptions and Parameters for LLM Tools (JSON)

Source: https://openrouter.ai/docs/guides/features/tool-calling

This JSON example showcases how to define a tool with a comprehensive description and detailed parameters for an LLM. A rich description helps the model understand the tool's capabilities and usage conditions, while well-structured parameters (including types, descriptions, enums, defaults, and required fields) guide the model in constructing valid tool calls.

```json
{
  "description": "Get current weather conditions and 5-day forecast for a specific location. Supports cities, zip codes, and coordinates.",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City name, zip code, or coordinates (lat,lng). Examples: 'New York', '10001', '40.7128,-74.0060'"
      },
      "units": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "Temperature unit preference",
        "default": "celsius"
      }
    },
    "required": ["location"]
  }
}
```

--------------------------------

### Use OpenAI SDK with OpenRouter as base URL

Source: https://openrouter.ai/docs/index

Configure the OpenAI SDK to use OpenRouter as the base URL endpoint, enabling compatibility with existing OpenAI code. Supports all OpenAI SDK features including streaming and includes optional attribution headers.

```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://openrouter.ai/api/v1',
  apiKey: '<OPENROUTER_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
    'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
  },
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: 'openai/gpt-5.2',
    messages: [
      {
        role: 'user',
        content: 'What is the meaning of life?',
      },
    ],
  });

  console.log(completion.choices[0].message);
}

main();
```

--------------------------------

### Example CompletionsResponse JSON

Source: https://openrouter.ai/docs/api/reference/overview

Demonstrates a complete example of a CompletionsResponse object with normalized finish_reason, usage statistics including token breakdowns and cost information, and model identifier. Shows the structure of a non-streaming response with a single choice containing an assistant message.

```json
{
  "id": "gen-xxxxxxxxxxxxxx",
  "choices": [
    {
      "finish_reason": "stop",
      "native_finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "Hello there!"
      }
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 4,
    "total_tokens": 14,
    "prompt_tokens_details": {
      "cached_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "cost": 0.00014
  },
  "model": "openai/gpt-3.5-turbo"
}
```

--------------------------------

### Update Guardrail - Go Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail

Go implementation using the net/http package to send a PATCH request. Demonstrates proper request construction and response handling in Go.

```APIDOC
### Go Implementation

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {
	url := "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000"

	payload := strings.NewReader("{\n  \"name\": \"Updated Guardrail Name\",\n  \"description\": \"Updated description\",\n  \"limit_usd\": 75,\n  \"reset_interval\": \"weekly\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))
}
```

**Usage Notes:**
- Replace `<token>` with your actual Bearer token
- Use `strings.NewReader()` to create the request body
- Always defer `res.Body.Close()` to prevent resource leaks
- Use `io.ReadAll()` to read the complete response body
```

--------------------------------

### Send chat completion request to OpenRouter API with Python

Source: https://openrouter.ai/docs/quickstart

Make a POST request to OpenRouter's chat completions endpoint using the requests library. Requires API key in Authorization header and accepts optional site attribution headers.

```python
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "HTTP-Referer": "<YOUR_SITE_URL>",
    "X-Title": "<YOUR_SITE_NAME>",
  },
  data=json.dumps({
    "model": "openai/gpt-5.2",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)
```

--------------------------------

### Call OpenRouter API directly with HTTP requests

Source: https://openrouter.ai/docs/index

Make direct HTTP POST requests to OpenRouter's chat completions endpoint using the requests library. Requires Bearer token authentication and supports optional attribution headers for leaderboard rankings.

```python
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "openai/gpt-5.2", # Optional
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)
```

--------------------------------

### Update Guardrail - Java Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail

Java implementation using the Unirest library for HTTP requests. Demonstrates fluent API usage for building and executing PATCH requests.

```APIDOC
### Java Implementation

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Updated Guardrail Name\",\n  \"description\": \"Updated description\",\n  \"limit_usd\": 75,\n  \"reset_interval\": \"weekly\"\n}")
  .asString();

System.out.println(response.getStatus());
System.out.println(response.getBody());
```

**Usage Notes:**
- Replace `<token>` with your actual Bearer token
- Add Unirest dependency to your project: `com.mashape.unirest:unirest-java`
- Use method chaining for fluent API
- Call `asString()` to get the response as a String
```

--------------------------------

### Update Guardrail - Swift Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail

Swift implementation using URLSession for HTTP requests. Shows how to configure headers, serialize JSON, and handle responses in Swift.

```APIDOC
### Swift Implementation

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]

let parameters = [
  "name": "Updated Guardrail Name",
  "description": "Updated description",
  "limit_usd": 75,
  "reset_interval": "weekly"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse as Any)
    if let data = data {
      let json = try? JSONSerialization.jsonObject(with: data, options: [])
      print(json as Any)
    }
  }
})

dataTask.resume()
```

**Usage Notes:**
- Replace `<token>` with your actual Bearer token
- Use `JSONSerialization` to convert dictionary to JSON data
- Set appropriate timeout interval for your use case
- Always call `resume()` on the data task to start the request
- Handle errors in the completion handler
```

--------------------------------

### Retrieve User Credits from OpenRouter API

Source: https://openrouter.ai/docs/api/api-reference/credits/get-credits

These code examples demonstrate how to make a GET request to the OpenRouter API's `/credits` endpoint to retrieve the authenticated user's total purchased and used credits. Each example uses a different programming language and requires an API key provided as a Bearer token in the Authorization header.

```python
import requests

url = "https://openrouter.ai/api/v1/credits"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/credits';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/credits"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/credits")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/credits")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/credits', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/credits");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/credits")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### POST /api/v1/chat/completions

Source: https://openrouter.ai/docs/index

Send a chat completion request to OpenRouter's unified API endpoint. This endpoint accepts messages and returns AI-generated responses, supporting both streaming and non-streaming modes. Compatible with OpenAI's API format.

```APIDOC
## POST /api/v1/chat/completions

### Description
Send a chat completion request to OpenRouter's unified API. This endpoint provides access to hundreds of AI models through a single interface with automatic fallback handling and cost optimization.

### Method
POST

### Endpoint
https://openrouter.ai/api/v1/chat/completions

### Headers
- **Authorization** (string) - Required - Bearer token with your OpenRouter API key
- **HTTP-Referer** (string) - Optional - Your site URL for rankings on openrouter.ai
- **X-Title** (string) - Optional - Your site name for rankings on openrouter.ai

### Request Body
- **model** (string) - Optional - Model identifier (e.g., 'openai/gpt-5.2')
- **messages** (array) - Required - Array of message objects with role and content
  - **role** (string) - Required - Message role ('user', 'assistant', 'system')
  - **content** (string) - Required - Message content
- **stream** (boolean) - Optional - Enable streaming responses (default: false)

### Request Example
```json
{
  "model": "openai/gpt-5.2",
  "messages": [
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ],
  "stream": false
}
```

### Response
#### Success Response (200)
- **choices** (array) - Array of completion choices
  - **message** (object) - The generated message
    - **role** (string) - Message role
    - **content** (string) - Generated message content
- **model** (string) - Model used for completion
- **usage** (object) - Token usage information

#### Response Example
```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "The meaning of life is a philosophical question..."
      }
    }
  ],
  "model": "openai/gpt-5.2"
}
```
```

--------------------------------

### Fetch OpenRouter API Keys - PHP

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Uses the Guzzle HTTP client library to make an authenticated GET request to the OpenRouter API. Requires Guzzle to be installed via Composer and returns the response body.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Update Guardrail - PHP Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail

PHP implementation using the Guzzle HTTP client library. Shows how to configure the request and handle the response in PHP.

```APIDOC
### PHP Implementation

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000', [
  'body' => '{
  "name": "Updated Guardrail Name",
  "description": "Updated description",
  "limit_usd": 75,
  "reset_interval": "weekly"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
?>
```

**Usage Notes:**
- Replace `<token>` with your actual Bearer token
- Ensure Guzzle is installed via Composer: `composer require guzzlehttp/guzzle`
- Use `getBody()` to retrieve the response content
- Wrap in try-catch for error handling
```

--------------------------------

### SDK Implementation - Go

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

Go implementation using the net/http package to create an API key with proper request configuration.

```APIDOC
```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/keys"

	payload := strings.NewReader("{\n  \"name\": \"Analytics Service Key\",\n  \"limit\": 150,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true,\n  \"expires_at\": \"2028-06-30T23:59:59Z\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```
```

--------------------------------

### Fetch OpenRouter API Keys - Python

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Uses the requests library to make an authenticated GET request to the OpenRouter API keys endpoint. Returns JSON response containing key information. Requires the requests package to be installed.

```python
import requests

url = "https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

--------------------------------

### Make an authenticated GET request to OpenRouter API endpoint

Source: https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints

These examples demonstrate how to perform an authenticated GET request to the OpenRouter API to fetch data from a specified endpoint. The common pattern involves constructing the request URL, adding an 'Authorization' header with a 'Bearer <token>' for authentication, and then executing the GET request using each language's respective HTTP client library. The output is typically the JSON response from the API.

```python
import requests

url = "https://openrouter.ai/api/v1/models/author/slug/endpoints"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/models/author/slug/endpoints';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/models/author/slug/endpoints"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/models/author/slug/endpoints")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models/author/slug/endpoints")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models/author/slug/endpoints', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/models/author/slug/endpoints");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models/author/slug/endpoints")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Fetch Models List - Go with HTTP Client

Source: https://openrouter.ai/docs/api/api-reference/models/get-models

Implements HTTP GET request using Go's standard library net/http package. Creates a new request with Authorization header and reads the response body. Demonstrates proper resource cleanup with defer.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/models"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Retrieve OpenRouter API Generation Data via GET Request

Source: https://openrouter.ai/docs/api/api-reference/generations/get-generation

These examples demonstrate how to fetch specific generation data from the OpenRouter API's `/api/v1/generation` endpoint. Each snippet performs a GET request, including an Authorization header with a bearer token and a query parameter for the generation ID. The response typically contains detailed generation information in JSON format.

```python
import requests

url = "https://openrouter.ai/api/v1/generation"

querystring = {"id":"id"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/generation?id=id';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/generation?id=id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/generation?id=id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/generation?id=id")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/generation?id=id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/generation?id=id");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/generation?id=id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Send chat completion request to OpenRouter API with curl

Source: https://openrouter.ai/docs/quickstart

Make a POST request to OpenRouter's chat completions endpoint using curl command-line tool. Requires API key in Authorization header and JSON payload with model and messages.

```shell
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -d '{
  "model": "openai/gpt-5.2",
  "messages": [
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
}'
```

--------------------------------

### Send API Request to OpenRouter AI - Ruby

Source: https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages

Ruby example using the Net::HTTP library to send a POST request to OpenRouter AI's messages endpoint. Includes SSL configuration, request header setup, and response body output.

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/messages")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"max_tokens\": 1024,\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"temperature\": 0.7\n}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Fetch Models Count via HTTP GET Request - PHP

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

PHP implementation using the Guzzle HTTP client library to make a GET request to the OpenRouter API. Requires Guzzle to be installed via Composer and includes Bearer token authentication.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models/count', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Manually Install OpenRouter SDK Skill

Source: https://openrouter.ai/docs/sdks/agentic-usage

Manually install the OpenRouter SDK skill by creating a .skills directory and downloading the skill file from the GitHub repository. This is an alternative to using the add-skill command.

```bash
mkdir -p .skills
curl -o .skills/openrouter-sdk.md \
  https://raw.githubusercontent.com/OpenRouterTeam/agent-skills/main/skills/typescript-sdk/SKILL.md
```

--------------------------------

### Start Mastra development server

Source: https://openrouter.ai/docs/community/mastra

Run the Mastra development server to start the application. This makes the agent available via REST API and interactive playground at localhost:4111.

```bash
npm run dev
```

--------------------------------

### Integrate Multiple Skill Tools with OpenRouter Model

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

Demonstrates a complete example combining skill discovery, skill loading, and multi-skill orchestration with OpenRouter's Claude model. Uses stepCountIs to limit execution steps and retrieves the final text result from the model's response.

```typescript
import { OpenRouter, tool, stepCountIs } from '@openrouter/sdk';
import { readFileSync, existsSync, readdirSync } from 'fs';
import path from 'path';
import { z } from 'zod';

const openrouter = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

const SKILLS_DIR = path.join(process.env.HOME || '~', '.claude', 'skills');

// ... (include skillsTool, multiSkillLoader, skillDiscoveryTool from above)

// Use all skill tools together
const result = openrouter.callModel({
  model: 'anthropic/claude-sonnet-4.5',
  input: `I have a complex task:
1. First, show me what skills are available
2. Load the appropriate skills for PDF analysis
3. Then help me extract and analyze data from report.pdf`,
  tools: [skillDiscoveryTool, skillsTool, multiSkillLoader],
  stopWhen: stepCountIs(10),
});

const text = await result.getText();
console.log(text);
```

--------------------------------

### Guide Model Responses with Assistant Prefill in OpenRouter API (TypeScript)

Source: https://openrouter.ai/docs/api/reference/overview

This TypeScript `fetch` request demonstrates how to use the assistant prefill feature in OpenRouter by including a partial assistant message at the end of the `messages` array. This technique helps guide the model to complete a response in a desired manner. It's useful for controlling the model's output and ensuring specific phrasing.

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    Authorization: 'Bearer <OPENROUTER_API_KEY>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'openai/gpt-5.2',
    messages: [
      { role: 'user', content: 'What is the meaning of life?' },
      { role: 'assistant', content: "I'm not sure, but my best guess is" },
    ],
  }),
});
```

--------------------------------

### Install OpenRouter SDK Skill via npm

Source: https://openrouter.ai/docs/sdks/agentic-usage

Install the OpenRouter SDK skill for AI coding assistants using the add-skill command. This command installs the skill in your project directory and enables AI agents to understand the SDK's APIs and patterns.

```bash
npx add-skill OpenRouterTeam/agent-skills
```

--------------------------------

### Update Guardrail - C# Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail

C# implementation using the RestSharp library for HTTP requests. Demonstrates request configuration and parameter handling in C#.

```APIDOC
### C# Implementation

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Updated Guardrail Name\",\n  \"description\": \"Updated description\",\n  \"limit_usd\": 75,\n  \"reset_interval\": \"weekly\"\n}", ParameterType.RequestBody);

IRestResponse response = client.Execute(request);

Console.WriteLine(response.StatusCode);
Console.WriteLine(response.Content);
```

**Usage Notes:**
- Replace `<token>` with your actual Bearer token
- Install RestSharp NuGet package: `Install-Package RestSharp`
- Use `AddParameter()` with `ParameterType.RequestBody` for JSON body
- Check `response.StatusCode` for HTTP status
```

--------------------------------

### Start Claude Code session with OpenRouter

Source: https://openrouter.ai/docs/guides/guides/claude-code-integration

Navigate to your project directory and start Claude Code to begin routing prompts through OpenRouter. Ensure environment variables are configured before running this command.

```bash
cd /path/to/your/project
claude
```

--------------------------------

### Send API Request to OpenRouter AI - PHP

Source: https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages

PHP example using the Guzzle HTTP client library to send a POST request to OpenRouter AI's messages endpoint. Includes autoloader setup, client instantiation, and response body output.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/messages', [
  'body' => '{
  "model": "anthropic/claude-4.5-sonnet-20250929",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": "Hello, how are you?"
    }
  ],
  "temperature": 0.7
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### List Providers with OpenRouter SDK (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/providers

This example demonstrates how to initialize the OpenRouter SDK using an API key and then call the `providers.list()` method. It retrieves and logs a list of all available providers from the OpenRouter API.

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.providers.list();

  console.log(result);
}

run();
```

--------------------------------

### Fetch Guardrail Assignment Members - PHP

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrail-member-assignments

Uses the Guzzle HTTP client library to make an authenticated GET request. Requires Guzzle dependency installed via Composer. Returns response body containing member data.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/members', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

--------------------------------

### SDK Implementation - JavaScript

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

JavaScript implementation using the Fetch API to create an API key with configuration parameters.

```APIDOC
```javascript
const url = 'https://openrouter.ai/api/v1/keys';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"name":"Analytics Service Key","limit":150,"limit_reset":"monthly","include_byok_in_limit":true,"expires_at":"2028-06-30T23:59:59Z"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```
```

--------------------------------

### Send API Request to OpenRouter AI - Python

Source: https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages

Python example using the requests library to send a POST request to OpenRouter AI's messages endpoint. Includes bearer token authentication, JSON payload with model configuration, and response parsing. Requires the requests library to be installed.

```python
import requests

url = "https://openrouter.ai/api/v1/messages"

payload = {
    "model": "anthropic/claude-4.5-sonnet-20250929",
    "max_tokens": 1024,
    "messages": [
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ],
    "temperature": 0.7
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

--------------------------------

### Set up viem Public and Wallet Clients

Source: https://openrouter.ai/docs/guides/guides/crypto-api

Initialize viem clients for interacting with the Base blockchain. The publicClient is used for read operations and transaction simulation, while the walletClient handles transaction signing and submission. Requires a private key for account creation.

```typescript
const publicClient = createPublicClient({
  chain: base,
  transport: http(),
});
const account = privateKeyToAccount('0x...');
const walletClient = createWalletClient({
  chain: base,
  transport: http(),
  account,
});
```

--------------------------------

### Get Generation Metadata with Standalone Function (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/generations

This TypeScript example illustrates fetching generation metadata using the standalone `generationsGetGeneration` function for optimized tree-shaking. It uses `OpenRouterCore` and includes explicit error handling for the API response.

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { generationsGetGeneration } from "@openrouter/sdk/funcs/generationsGetGeneration.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await generationsGetGeneration(openRouter, {
    id: "<id>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("generationsGetGeneration failed:", res.error);
  }
}

run();
```

--------------------------------

### Initialize Debug Object in OpenRouter TypeScript SDK

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/debug

This example demonstrates how to import the `Debug` type from the OpenRouter TypeScript SDK and initialize an empty `Debug` object. This is a basic setup for using the `Debug` functionality within your TypeScript application.

```typescript
import { Debug } from "@openrouter/sdk/models";

let value: Debug = {};
```

--------------------------------

### Guardrail Configuration Example with Spending Limits

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createguardraildata

Example JSON payload demonstrating a production guardrail configuration with spending limits, provider restrictions, and specific model allowlisting. Shows practical usage of the guardrail fields with realistic values for USD limits, reset intervals, and provider/model constraints.

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Production Guardrail",
  "description": "Guardrail for production environment",
  "limitUsd": 100,
  "resetInterval": "monthly",
  "allowedProviders": [
    "openai",
    "anthropic",
    "google"
  ],
  "allowedModels": [
    "openai/gpt-5.2-20251211",
    "anthropic/claude-4.5-opus-20251124",
    "deepseek/deepseek-r1-0528:free"
  ],
  "enforceZdr": false,
  "createdAt": "2025-08-24T10:30:00Z",
  "updatedAt": "2025-08-24T15:45:00Z"
}
```

--------------------------------

### Make an API Call to OpenRouter with Tool Use

Source: https://openrouter.ai/docs/api/api-reference/responses/create-responses

These examples illustrate how to send a POST request to the OpenRouter API's /api/v1/responses endpoint. Each snippet includes a user message and a tool definition, demonstrating how to configure the request body with an authorization token and JSON content type. The API call is designed to get a response from a specified model, potentially utilizing the defined tool.

```python
import requests

url = "https://openrouter.ai/api/v1/responses"

payload = {
    "input": [
        {
            "type": "message",
            "role": "user",
            "content": "Hello, how are you?"
        }
    ],
    "tools": [
        {
            "type": "function",
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": { "location": { "type": "string" } }
            }
        }
    ],
    "model": "anthropic/claude-4.5-sonnet-20250929",
    "temperature": 0.7,
    "top_p": 0.9
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/responses';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"input":[{"type":"message","role":"user","content":"Hello, how are you?"}],"tools":[{"type":"function","name":"get_current_weather","description":"Get the current weather in a given location","parameters":{"type":"object","properties":{"location":{"type":"string"}}}}],"model":"anthropic/claude-4.5-sonnet-20250929","temperature":0.7,"top_p":0.9}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/responses"

	payload := strings.NewReader("{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"
          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}")
	req, _ := http.NewRequest("POST", url, payload)
	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)
	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/responses")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"
          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/responses")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"
          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/responses', [
  'body' => '{
  "input": [
    {
      "type": "message",
      "role": "user",
      "content": "Hello, how are you?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {

```

--------------------------------

### Best Practice: Add Descriptions to OpenRouter AI Tool Input Schemas (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/call-model/tools

This example demonstrates the best practice of using `.describe()` on Zod schema fields to provide detailed explanations for each input parameter. These descriptions offer crucial context to the model, helping it understand the purpose, constraints, and expected values for tool arguments.

```typescript
const inputSchema = z.object({
  query: z.string().describe('Natural language search query'),
  maxResults: z.number()
    .min(1)
    .max(100)
    .default(10)
    .describe('Maximum number of results to return (1-100)'),
  dateRange: z.enum(['day', 'week', 'month', 'year', 'all'])
    .default('all')
    .describe('Filter results by time period'),
});
```

--------------------------------

### Send API Request to OpenRouter AI - Swift

Source: https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages

Swift example using URLSession to send a POST request to OpenRouter AI's messages endpoint. Includes NSMutableURLRequest configuration, JSON serialization, header setup, and asynchronous response handling with error checking.

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "model": "anthropic/claude-4.5-sonnet-20250929",
  "max_tokens": 1024,
  "messages": [
    [
      "role": "user",
      "content": "Hello, how are you?"
    ]
  ],
  "temperature": 0.7
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/messages")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})
```

--------------------------------

### Install Effect AI SDK and OpenRouter Integration Packages (npm)

Source: https://openrouter.ai/docs/community/effect-ai-sdk

This command installs the core Effect library, the Effect AI SDK abstractions, the OpenRouter integration for Effect AI, and platform-agnostic utilities. These packages are essential for setting up an Effect application to interact with OpenRouter's language models.

```bash
npm install effect @effect/ai @effect/ai-openrouter @effect/platform
```

--------------------------------

### Install PydanticAI for OpenAI-Compatible LLMs

Source: https://openrouter.ai/docs/community/pydantic-ai

This command installs the `pydantic-ai-slim` library, including its OpenAI-specific dependencies. These dependencies are crucial for integrating with OpenAI-compatible APIs like OpenRouter, ensuring all required packages are available for LLM interactions.

```bash
pip install 'pydantic-ai-slim[openai]'
```

--------------------------------

### Send API Request to OpenRouter AI - Java

Source: https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages

Java example using the Unirest HTTP client library to send a POST request to OpenRouter AI's messages endpoint. Includes header configuration and JSON body payload setup with synchronous response handling.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/messages")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"max_tokens\": 1024,\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"temperature\": 0.7\n}")
  .asString();
```

--------------------------------

### Send API Request to OpenRouter AI - C#

Source: https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages

C# example using the RestSharp library to send a POST request to OpenRouter AI's messages endpoint. Includes RestClient setup, request method configuration, header addition, and JSON body parameter handling.

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/messages");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"max_tokens\": 1024,\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"temperature\": 0.7\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Install Claude Code via Native Shell Script

Source: https://openrouter.ai/docs/guides/guides/claude-code-integration

Install Claude Code on macOS, Linux, or WSL using a shell script. This is the recommended installation method and downloads the latest version directly from Claude's installation endpoint.

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

--------------------------------

### Get Generation Metadata with OpenRouter SDK (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/generations

This TypeScript example demonstrates how to retrieve request and usage metadata for a specific generation using the `OpenRouter` client. It initializes the SDK with an API key and calls the `generations.getGeneration` method, passing the generation ID.

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.generations.getGeneration({
    id: "<id>",
  });

  console.log(result);
}

run();
```

--------------------------------

### Create PDF Processing Skill Definition

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

Example skill file that defines PDF processing capabilities. This markdown file is loaded by the skills tool and injected into the conversation context to provide the model with specialized instructions.

```markdown
# PDF Processing Skill

You are now equipped with PDF processing capabilities.

## Available Tools
When processing PDFs, you have access to:
- `extract_text`: Extract all text from a PDF
- `extract_tables`: Extract tables as structured data
- `extract_images`: Extract embedded images
- `split_pdf`: Split PDF into individual pages
```

--------------------------------

### Create Skills Directory Structure

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

Set up the directory structure for storing skill definitions. Creates separate directories for different skill types like PDF processing, data analysis, and code review.

```bash
mkdir -p ~/.claude/skills/pdf-processing
mkdir -p ~/.claude/skills/data-analysis
mkdir -p ~/.claude/skills/code-review
```

--------------------------------

### Python Example - Chat Completion with Thinking Levels

Source: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens

Python code example using the OpenAI client library to interact with Google Gemini 3 models via OpenRouter with reasoning effort levels. Demonstrates how to extract reasoning and content from the response.

```APIDOC
## Python Implementation Example

### Description
Python example using OpenAI client library to create chat completions with Google Gemini 3 models and reasoning effort levels.

### Code
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_API_KEY",
)

response = client.chat.completions.create(
    model="google/gemini-3-pro-preview",
    messages=[
        {"role": "user", "content": "Explain the implications of quantum entanglement."}
    ],
    extra_body={
        "reasoning": {
            "effort": "low"  # Maps to thinkingLevel: "low"
        }
    },
)

msg = response.choices[0].message
print("Reasoning:", getattr(msg, "reasoning", None))
print("Content:", getattr(msg, "content", None))
```

### Usage Notes
- The `extra_body` parameter passes the reasoning configuration to the API
- Use `getattr()` to safely access the reasoning attribute which may not always be present
- The effort level "low" provides moderate reasoning depth for balanced performance
```

--------------------------------

### List all models and their properties using OpenRouter Python SDK

Source: https://openrouter.ai/docs/sdks/python/api-reference/models/models

This example shows how to fetch a list of all available models and their properties from the OpenRouter API using the Python SDK. It sets up the OpenRouter client with an API key, usually from an environment variable, and then invokes the `models.list()` method. The retrieved list of models is subsequently printed.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.models.list()

    # Handle response
    print(res)
```

--------------------------------

### Example OpenRouter API Response with Reasoning (JSON)

Source: https://openrouter.ai/docs/api/reference/responses/reasoning

This JSON example illustrates the structure of a successful response from the OpenRouter API when reasoning is enabled. It shows how reasoning information, including encrypted content and a summary of steps, is included in the `output` array. The example also details `usage` statistics, specifically `reasoning_tokens`.

```json
{
  "id": "resp_1234567890",
  "object": "response",
  "created_at": 1234567890,
  "model": "openai/o4-mini",
  "output": [
    {
      "type": "reasoning",
      "id": "rs_abc123",
      "encrypted_content": "gAAAAABotI9-FK1PbhZhaZk4yMrZw3XDI1AWFaKb9T0NQq7LndK6zaRB...",
      "summary": [
        "First, I need to determine the current year",
        "Then calculate the difference from 1995",
        "Finally, compare that to 30 years"
      ]
    },
    {
      "type": "message",
      "id": "msg_xyz789",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "Yes. In 2025, 1995 was 30 years ago. In fact, as of today (Aug 31, 2025), it's exactly 30 years since Aug 31, 1995.",
          "annotations": []
        }
      ]
    }
  ],
  "usage": {
    "input_tokens": 15,
    "output_tokens": 85,
    "output_tokens_details": {
      "reasoning_tokens": 45
    },
    "total_tokens": 100
  },
  "status": "completed"
}
```

--------------------------------

### Install Arize and OpenInference Dependencies

Source: https://openrouter.ai/docs/guides/community/arize

Install required packages for Arize integration with OpenInference instrumentation and OpenAI SDK. This command installs the OpenInference instrumentation for OpenAI, the OpenAI Python client, and Arize's OpenTelemetry components.

```bash
pip install openinference-instrumentation-openai openai arize-otel
```

--------------------------------

### Create a response using OpenRouter TypeScript SDK instance

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/responses

This example demonstrates how to initialize the OpenRouter SDK with an API key and then use the `beta.responses.send` method to create a response. The result of the operation is logged to the console.

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.beta.responses.send({});

  console.log(result);
}

run();
```

--------------------------------

### Python Example - Debug Chat Completions

Source: https://openrouter.ai/docs/api/reference/errors-and-debugging

Complete Python example showing how to make a debug-enabled request to OpenRouter's Chat Completions API and parse the streaming response.

```APIDOC
## Python Implementation

### Description
Python example for calling the Chat Completions API with debug mode enabled and processing the streaming response.

### Code
```python
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "anthropic/claude-haiku-4.5",
    "stream": True,
    "messages": [
      { "role": "system", "content": "You are a helpful assistant." },
      { "role": "user", "content": "Hello!" }
    ],
    "debug": {
      "echo_upstream_body": True
    }
  }),
  stream=True
)

for line in response.iter_lines():
  if line:
    text = line.decode('utf-8')
    if 'echo_upstream_body' in text:
      print(text)
```

### Key Points
- Use requests library with stream=True for streaming responses
- Iterate through response lines using iter_lines()
- Decode bytes to UTF-8 strings
- Filter for lines containing debug information
- Display debug chunks for inspection
```

--------------------------------

### Create API Key with OpenRouter API - Go

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

Go implementation using the net/http package to make an authenticated POST request to create an API key. Demonstrates proper resource cleanup with defer statement and JSON payload construction using strings.NewReader.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/keys"

	payload := strings.NewReader("{\n  \"name\": \"Analytics Service Key\",\n  \"limit\": 150,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true,\n  \"expires_at\": \"2028-06-30T23:59:59Z\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### SDK Implementation - Ruby

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

Ruby implementation using Net::HTTP to create an API key with SSL support.

```APIDOC
```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Analytics Service Key\",\n  \"limit\": 150,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true,\n  \"expires_at\": \"2028-06-30T23:59:59Z\"\n}"

response = http.request(request)
puts response.read_body
```
```

--------------------------------

### Credits API Response - JSON

Source: https://openrouter.ai/docs/api-reference/get-credits

Example JSON response from the credits endpoint containing total credits purchased and total usage. The data object includes total_credits and total_usage numeric properties.

```json
{
  "data": {
    "total_credits": 100.5,
    "total_usage": 25.75
  }
}
```

--------------------------------

### Install LiveKit Agents with OpenAI Plugin

Source: https://openrouter.ai/docs/guides/community/livekit

Install the OpenAI plugin package to add OpenRouter support to LiveKit Agents. This command installs version 1.2 or compatible versions of the livekit-agents package with OpenAI plugin support.

```bash
uv add "livekit-agents[openai]~=1.2"
```

--------------------------------

### Get Generation Metadata using OpenRouter Python SDK

Source: https://openrouter.ai/docs/sdks/python/api-reference/generations

This example demonstrates how to retrieve request and usage metadata for a specific generation using the OpenRouter Python SDK. It initializes the client with an API key, typically from an environment variable, and then calls the `get_generation` method with a generation ID to fetch the details.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.generations.get_generation(id="<id>")

    # Handle response
    print(res)
```

--------------------------------

### Initialize Viem Clients and Import Dependencies for Transaction Execution

Source: https://openrouter.ai/docs/guides/guides/crypto-api

Sets up public and wallet clients using viem library with Base network configuration. Imports account creation from private key and ether parsing utilities. This foundation enables transaction signing and broadcasting on the Base blockchain.

```typescript
import { createPublicClient, createWalletClient, http, parseEther } from 'viem';
import { privateKeyToAccount } from 'viem/accounts';
import { base } from 'viem/chains';
```

--------------------------------

### List Models for User (Python SDK)

Source: https://openrouter.ai/docs/sdks/python/api-reference/models/models

This Python example demonstrates how to initialize the OpenRouter client and call the `list_for_user` method. It requires the `openrouter` SDK and uses an environment variable for the bearer token to handle authentication. The response object, containing the list of models, is then printed to the console.

```python
from openrouter import OpenRouter, operations
import os

with OpenRouter() as open_router:

    res = open_router.models.list_for_user(security=operations.ListModelsUserSecurity(
        bearer=os.getenv("OPENROUTER_BEARER", ""),
    ))

    # Handle response
    print(res)
```

--------------------------------

### List Available Embeddings Models Programmatically

Source: https://openrouter.ai/docs/api/reference/embeddings

This collection of code examples demonstrates how to retrieve a list of all available embedding models from the OpenRouter API. It includes implementations using the OpenRouter TypeScript SDK, a direct Python HTTP request, the TypeScript fetch API, and a shell command. The examples show how to authenticate with an API key and parse the JSON response to display model details.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '{{API_KEY_REF}}',
});

const models = await openRouter.embeddings.listModels();
console.log(models.data);
```

```python
import requests

response = requests.get(
  "https://openrouter.ai/api/v1/embeddings/models",
  headers={
    "Authorization": f"Bearer {{API_KEY_REF}}",
  }
)

models = response.json()
for model in models["data"]:
  print(f"{model['id']}: {model.get('context_length', 'N/A')} tokens")
```

```typescript
const response = await fetch('https://openrouter.ai/api/v1/embeddings/models', {
  headers: {
    'Authorization': 'Bearer {{API_KEY_REF}}',
  },
});

const models = await response.json();
console.log(models.data);
```

```shell
curl https://openrouter.ai/api/v1/embeddings/models \
  -H "Authorization: Bearer $OPENROUTER_API_KEY"
```

--------------------------------

### Install Claude Code via Windows PowerShell

Source: https://openrouter.ai/docs/guides/guides/claude-code-integration

Install Claude Code on Windows using PowerShell. This method downloads and executes the installation script from Claude's endpoint.

```powershell
irm https://claude.ai/install.ps1 | iex
```

--------------------------------

### Multi-Step Research Request with Interleaved Thinking

Source: https://openrouter.ai/docs/guides/features/tool-calling

JSON request demonstrating how to configure a model with interleaved thinking for multi-step research. Includes model selection, user message, and tool definitions for searching academic papers and retrieving statistics. This example shows the initial setup for a comprehensive analysis workflow.

```json
{
  "model": "anthropic/claude-sonnet-4.5",
  "messages": [
    {
      "role": "user",
      "content": "Research the environmental impact of electric vehicles and provide a comprehensive analysis."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "search_academic_papers",
        "description": "Search for academic papers on a given topic",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {"type": "string"},
            "field": {"type": "string"}
          },
          "required": ["query"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "get_latest_statistics",
        "description": "Get latest statistics on a topic",
        "parameters": {
          "type": "object",
          "properties": {
            "topic": {"type": "string"},
            "year": {"type": "integer"}
          },
          "required": ["topic"]
        }
      }
    }
  ]
}
```

--------------------------------

### Retrieve Full Model Response Object with Usage Data (TypeScript)

Source: https://openrouter.ai/docs/sdks/call-model/text-generation

This example shows how to get the complete response object from `callModel` using `getResponse()`, which includes the full output array and detailed token usage information for input, output, and cached tokens.

```typescript
const response = await result.getResponse();

console.log(response.output);     // Full output array
console.log(response.usage);      // Token usage information

// Usage includes:
// - inputTokens: tokens in the prompt
// - outputTokens: tokens generated
// - cachedTokens: tokens served from cache (cost savings)
```

--------------------------------

### Streaming Response Example

Source: https://openrouter.ai/docs/best-practices/reasoning-tokens

Demonstrates how reasoning_details appears in streaming API responses. Shows how reasoning details are delivered incrementally in delta chunks as the reasoning is generated.

```APIDOC
## Streaming Response

### Description
In streaming responses, `reasoning_details` appears in delta chunks as the reasoning is generated progressively.

### Response Structure
```json
{
  "choices": [
    {
      "delta": {
        "reasoning_details": [
          {
            "type": "reasoning.text",
            "text": "Let me think about this step by step...",
            "signature": null,
            "id": "reasoning-text-1",
            "format": "anthropic-claude-v1",
            "index": 0
          }
        ]
      }
    }
  ]
}
```

### Streaming Behavior Notes
- Each reasoning detail chunk is sent as it becomes available
- The `reasoning_details` array in each chunk may contain one or more reasoning objects
- For encrypted reasoning, the content may appear as `[REDACTED]` in streaming responses
- The complete reasoning sequence is built by concatenating all chunks in order
```

--------------------------------

### Call Model with Multiple Tools in OpenRouter SDK

Source: https://openrouter.ai/docs/sdks/typescript/call-model/tools

This example shows how to provide an array of multiple tools to the `openrouter.callModel` method. The language model can then intelligently select and utilize the appropriate tools from the provided list to fulfill complex requests.

```typescript
const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  input: 'Search for TypeScript tutorials and calculate 2+2',
  tools: [searchTool, calculatorTool],
});
```

--------------------------------

### Retrieve User Credits with OpenRouter Python SDK

Source: https://openrouter.ai/docs/sdks/python/api-reference/credits

This Python example demonstrates how to fetch the total credits purchased and used by an authenticated user. It initializes the OpenRouter client with an API key from environment variables and then calls the `get_credits` method. The response, containing credit details, is printed to the console.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.credits.get_credits()

    # Handle response
    print(res)

```

--------------------------------

### Install Langfuse and OpenAI SDK

Source: https://openrouter.ai/docs/community/langfuse

Install required Python packages for Langfuse integration with OpenAI SDK. This provides the foundation for automatic tracing of OpenRouter API calls.

```bash
pip install langfuse openai
```

--------------------------------

### List OpenRouter API Keys

Source: https://openrouter.ai/docs/guides/overview/auth/management-api-keys

Demonstrates how to retrieve a list of OpenRouter API keys. Examples include fetching the most recent 100 keys and paginating results using an offset parameter. A Management API key is required for authorization.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: 'your-management-key', // Use your Management API key
});

// List the most recent 100 API keys
const keys = await openRouter.apiKeys.list();

// You can paginate using the offset parameter
const keysPage2 = await openRouter.apiKeys.list({ offset: 100 });
```

```python
import requests

MANAGEMENT_API_KEY = "your-management-key"
BASE_URL = "https://openrouter.ai/api/v1/keys"

# List the most recent 100 API keys
response = requests.get(
    BASE_URL,
    headers={
        "Authorization": f"Bearer {MANAGEMENT_API_KEY}",
        "Content-Type": "application/json"
    }
)

# You can paginate using the offset parameter
response = requests.get(
    f"{BASE_URL}?offset=100",
    headers={
        "Authorization": f"Bearer {MANAGEMENT_API_KEY}",
        "Content-Type": "application/json"
    }
)
```

```typescript
const MANAGEMENT_API_KEY = 'your-management-key';
const BASE_URL = 'https://openrouter.ai/api/v1/keys';

// List the most recent 100 API keys
const listKeys = await fetch(BASE_URL, {
  headers: {
    Authorization: `Bearer ${MANAGEMENT_API_KEY}`,
    'Content-Type': 'application/json',
  },
});

// You can paginate using the `offset` query parameter
const listKeys = await fetch(`${BASE_URL}?offset=100`, {
  headers: {
    Authorization: `Bearer ${MANAGEMENT_API_KEY}`,
    'Content-Type': 'application/json',
  },
});
```

--------------------------------

### Fetch OpenRouter API Keys - Go

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Uses the net/http package to create an HTTP GET request with custom headers and reads the response body. Demonstrates Go's standard library HTTP client usage with error handling.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### POST /api/v1/keys

Source: https://openrouter.ai/docs/guides/overview/auth/management-api-keys

Create a new API key with optional credit limit and configuration settings. Returns the newly created key details.

```APIDOC
## POST /api/v1/keys

### Description
Create a new API key for your account with optional credit limits and configuration options.

### Method
POST

### Endpoint
`https://openrouter.ai/api/v1/keys`

#### Headers
- **Authorization** (string) - Required - Bearer token with Management API key format: `Bearer {MANAGEMENT_API_KEY}`
- **Content-Type** (string) - Required - `application/json`

#### Request Body
- **name** (string) - Required - Name for the new API key
- **limit** (integer) - Optional - Credit limit for the key

### Request Example
```json
{
  "name": "Customer Instance Key",
  "limit": 1000
}
```

### Response
#### Success Response (201)
- **key_hash** (string) - Unique identifier for the created key
- **name** (string) - Name of the API key
- **limit** (integer) - Credit limit for the key
- **disabled** (boolean) - Whether the key is disabled

#### Response Example
```json
{
  "key_hash": "key_abc123",
  "name": "Customer Instance Key",
  "limit": 1000,
  "disabled": false
}
```
```

--------------------------------

### Illustrate ListKeyAssignmentsResponse structure in TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listkeyassignmentsresponse

This example demonstrates the structure of a `ListKeyAssignmentsResponse` object in TypeScript. It shows how to import the type and initialize a variable with sample data, including an array of key assignments and a total count. This helps developers understand the expected data format when working with the OpenRouter SDK.

```typescript
import { ListKeyAssignmentsResponse } from "@openrouter/sdk/models/operations";

let value: ListKeyAssignmentsResponse = {
  data: [
    {
      id: "550e8400-e29b-41d4-a716-446655440000",
      keyHash:
        "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93",
      guardrailId: "550e8400-e29b-41d4-a716-446655440001",
      keyName: "Production Key",
      keyLabel: "prod-key",
      assignedBy: "user_abc123",
      createdAt: "2025-08-24T10:30:00Z"
    }
  ],
  totalCount: 25
};
```

--------------------------------

### Configure Provider Sorting and Latency Preferences - Python

Source: https://openrouter.ai/docs/guides/routing/provider-selection

Set up OpenRouter API request with model selection, provider sorting by price, and preferred maximum latency constraints. This example demonstrates basic provider configuration with a single p90 latency percentile cutoff of 3 seconds.

```python
import requests

headers = {
  'Authorization': 'Bearer <OPENROUTER_API_KEY>',
  'Content-Type': 'application/json',
}

response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
  'models': [
    'anthropic/claude-sonnet-4.5',
    'openai/gpt-5-mini',
  ],
  'messages': [{ 'role': 'user', 'content': 'Hello' }],
  'provider': {
    'sort': {
      'by': 'price',
      'partition': 'none',
    },
    'preferred_max_latency': {
      'p90': 3,
    },
  },
})
```

--------------------------------

### Initialize OpenRouter Client and Chat Messages for Tool Calling

Source: https://openrouter.ai/docs/guides/features/tool-calling

This code snippet illustrates the initial setup required to interact with the OpenRouter API for tool calling. It involves importing necessary libraries, configuring the API key and desired model, and defining the system and user messages that will be sent to the LLM. Placeholders like `{{API_KEY_REF}}` and `{{MODEL}}` are used for dynamic values.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const OPENROUTER_API_KEY = "{{API_KEY_REF}}";

// You can use any model that supports tool calling
const MODEL = "{{MODEL}}";

const openRouter = new OpenRouter({
  apiKey: OPENROUTER_API_KEY,
});

const task = "What are the titles of some James Joyce books?";

const messages = [
  {
    role: "system",
    content: "You are a helpful assistant."
  },
  {
    role: "user",
    content: task,
  }
];
```

```python
import json, requests
from openai import OpenAI

OPENROUTER_API_KEY = f"{{API_KEY_REF}}"

# You can use any model that supports tool calling
MODEL = "{{MODEL}}"

openai_client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTER_API_KEY,
)

task = "What are the titles of some James Joyce books?"

messages = [
  {
    "role": "system",
    "content": "You are a helpful assistant."
  },
  {
    "role": "user",
    "content": task,
  }
]
```

```typescript
const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    Authorization: `Bearer {{API_KEY_REF}}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: '{{MODEL}}',
    messages: [
      { role: 'system', content: 'You are a helpful assistant.' },
      {
            role: 'user',
            content: 'What are the titles of some James Joyce books?',
          },
    ],
  }),
});
```

--------------------------------

### Configure LangChain ChatOpenAI with OpenRouter API in TypeScript

Source: https://openrouter.ai/docs/community/lang-chain

This TypeScript snippet demonstrates how to initialize and use the `ChatOpenAI` model from LangChain with OpenRouter's API. It configures the `baseURL` to OpenRouter, sets optional `HTTP-Referer` and `X-Title` headers for site ranking, and provides an example of invoking the chat model with system and human messages to get a response.

```typescript
import { ChatOpenAI } from "@langchain/openai";
import { HumanMessage, SystemMessage } from "@langchain/core/messages";

const chat = new ChatOpenAI(
  {
    model: '<model_name>',
    temperature: 0.8,
    streaming: true,
    apiKey: '${API_KEY_REF}',
  },
  {
    baseURL: 'https://openrouter.ai/api/v1',
    defaultHeaders: {
      'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
      'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
    },
  },
);

// Example usage
const response = await chat.invoke([
  new SystemMessage("You are a helpful assistant."),
  new HumanMessage("Hello, how are you?"),
]);
```

--------------------------------

### Find cheapest OpenRouter model by price with minimum throughput

Source: https://openrouter.ai/docs/guides/routing/provider-selection

This code demonstrates how to use OpenRouter's `provider` options to find the cheapest model across a list of specified models that also meets a minimum throughput requirement (e.g., 50 tokens/sec at p90). It uses `sort.by: 'price'` and `partition: 'none'` to search globally, and `preferredMinThroughput` to set the performance floor. This helps optimize cost while ensuring a baseline performance.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
});

const completion = await openRouter.chat.send({
  models: [
    'anthropic/claude-sonnet-4.5',
    'openai/gpt-5-mini',
    'google/gemini-3-flash-preview',
  ],
  messages: [{ role: 'user', content: 'Hello' }],
  provider: {
    sort: {
      by: 'price',
      partition: 'none',
    },
    preferredMinThroughput: {
      p90: 50, // Prefer providers with >50 tokens/sec for 90% of requests in last 5 minutes
    },
  },
  stream: false,
});
```

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer <OPENROUTER_API_KEY>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    models: [
      'anthropic/claude-sonnet-4.5',
      'openai/gpt-5-mini',
      'google/gemini-3-flash-preview',
    ],
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      sort: {
        by: 'price',
        partition: 'none',
      },
      preferred_min_throughput: {
        p90: 50, // Prefer providers with >50 tokens/sec for 90% of requests in last 5 minutes
      },
    },
  }),
});
```

```python
import requests

headers = {
  'Authorization': 'Bearer <OPENROUTER_API_KEY>',
  'Content-Type': 'application/json',
}

response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
  'models': [
    'anthropic/claude-sonnet-4.5',
    'openai/gpt-5-mini',
    'google/gemini-3-flash-preview',
  ],
  'messages': [{ 'role': 'user', 'content': 'Hello' }],
  'provider': {
    'sort': {
      'by': 'price',
      'partition': 'none',
    },
    'preferred_min_throughput': {
      'p90': 50, # Prefer providers with >50 tokens/sec for 90% of requests in last 5 minutes
    },
  },
})
```

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer <OPENROUTER_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "models": [
      "anthropic/claude-sonnet-4.5",
      "openai/gpt-5-mini",
      "google/gemini-3-flash-preview"
    ],
    "messages": [{ "role": "user", "content": "Hello" }],
    "provider": {
      "sort": {
        "by": "price",
        "partition": "none"
      },
      "preferred_min_throughput": {
        "p90": 50
      }
    }
  }'
```

--------------------------------

### Get User Activity with OpenRouter TypeScript SDK

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/analytics

Retrieves user activity data grouped by endpoint for the last 30 completed UTC days. Requires a provisioning API key for authentication. This example demonstrates the class-based approach using the OpenRouter SDK instance.

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.analytics.getUserActivity();

  console.log(result);
}

run();
```

--------------------------------

### Launch OpenRouter DevTools web interface via CLI (Bash)

Source: https://openrouter.ai/docs/sdks/dev-tools/devtools

Execute this command in your terminal to start the OpenRouter DevTools web interface. It launches a local server, typically on port 4983, and opens your browser to display real-time visualizations of captured SDK telemetry data, including runs, requests, token usage, and errors.

```bash
openrouter devtools
```

--------------------------------

### Create new Mastra project with CLI

Source: https://openrouter.ai/docs/community/mastra

Initialize a new Mastra project using the create-mastra command-line tool. This sets up the project structure with prompts for configuration including project name, components selection, and default provider choice.

```bash
npx create-mastra@latest
```

--------------------------------

### SDK Implementation - Java

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

Java implementation using Unirest library to create an API key with headers and request body.

```APIDOC
```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/keys")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Analytics Service Key\",\n  \"limit\": 150,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true,\n  \"expires_at\": \"2028-06-30T23:59:59Z\"\n}")
  .asString();
```
```

--------------------------------

### Second Tool Call - Get Latest Statistics

Source: https://openrouter.ai/docs/guides/features/tool-calling

Example of the second tool call after receiving initial research results. Retrieves current statistics on electric vehicle carbon footprint for 2024. Shows how the model chains tool calls based on reasoning about previous results.

```json
get_latest_statistics({
  "topic": "electric vehicle carbon footprint",
  "year": 2024
})
```

--------------------------------

### SDK Implementation - Swift

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

Swift implementation using URLSession to create an API key with JSON serialization and HTTP request configuration.

```APIDOC
```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "Analytics Service Key",
  "limit": 150,
  "limit_reset": "monthly",
  "include_byok_in_limit": true,
  "expires_at": "2028-06-30T23:59:59Z"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/keys")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
```

--------------------------------

### List API Keys - Go

Source: https://openrouter.ai/docs/api/api-reference/api-keys/list

Retrieve API keys using Go's net/http package. Creates an HTTP GET request with Bearer token header, executes it, and reads the response body. Prints response status and body content.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/keys"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### GET /keys

Source: https://openrouter.ai/docs/sdks/python/api-reference/apikeys

List all API keys for the authenticated user. Provisioning key required.

```APIDOC
## GET /keys

### Description
List all API keys for the authenticated user. Provisioning key required.

### Method
GET

### Endpoint
/keys

### Parameters
#### Query Parameters
- **include_disabled** (Optional[str]) - Optional - Whether to include disabled API keys in the response
- **offset** (Optional[str]) - Optional - Number of API keys to skip for pagination
- **retries** (Optional[utils.RetryConfig]) - Optional - Configuration to override the default retry behavior of the client.

### Response
#### Success Response (200)
- **response** (operations.ListResponse) - Successful response containing a list of API keys.

### Errors
- **errors.UnauthorizedResponseError** (401) - Unauthorized
- **errors.TooManyRequestsResponseError** (429) - Too Many Requests
- **errors.InternalServerResponseError** (500) - Internal Server Error
- **errors.OpenRouterDefaultError** (4XX, 5XX) - Generic API Error
```

--------------------------------

### Retrieve OpenRouter Guardrail Assignments for Members

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-member-assignments

These code snippets illustrate how to fetch guardrail assignments for members from the OpenRouter API. They all perform a GET request to the `/api/v1/guardrails/assignments/members` endpoint, requiring an `Authorization` header with a bearer token for authentication. The examples cover common HTTP client libraries in different languages.

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails/assignments/members"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails/assignments/members';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/guardrails/assignments/members"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/guardrails/assignments/members")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/guardrails/assignments/members")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/guardrails/assignments/members', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/guardrails/assignments/members");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails/assignments/members")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Backward Compatibility Reference

Source: https://openrouter.ai/docs/guides/guides/model-migrations/claude-4-6

Reference guide for backward compatibility between Claude 4.5 and Claude 4.6, showing how existing requests continue to work without changes.

```APIDOC
## Backward Compatibility

### Breaking Changes
None. Existing requests continue to work without modification.

### Feature Comparison

| Feature | Claude 4.5 Opus | Claude 4.6 Opus / Sonnet |
|---------|-----------------|-------------------------|
| Default Thinking Mode | Budget-based | Adaptive |
| `reasoning.max_tokens` | Budget-based | Budget-based |
| `verbosity: 'max'` | Falls back to `'high'` | Supported |
| `reasoning.effort` | Supported | Ignored (uses adaptive) |

### Migration Notes
- Budget-based thinking still works when `reasoning.max_tokens` is set
- `reasoning.effort` values (low, medium, high) are still supported for older models
- For Claude 4.6, `reasoning.effort` will be ignored; use `reasoning.max_tokens` for budget control
- Use `verbosity` to control Anthropic's `output_config.effort`
- Older models (4.5 Opus, 3.7 Sonnet, etc.) behave exactly as before

### Deprecated Parameters for Claude 4.6
- `reasoning.effort` - Use `reasoning.max_tokens` instead for budget control
- `verbosity: 'high'` - Can now use `verbosity: 'max'` for maximum effort
```

--------------------------------

### Retrieve Guardrail Assignment Keys from OpenRouter API

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrail-key-assignments

These examples illustrate how to fetch guardrail assignment keys from the OpenRouter API using a GET request. An authorization token is required in the header for successful authentication. The API endpoint is `https://openrouter.ai/api/v1/guardrails/{guardrail_id}/assignments/keys`.

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Uninstall OpenAI and install OpenRouter provider

Source: https://openrouter.ai/docs/community/mastra

Remove the default OpenAI SDK package and install the OpenRouter AI SDK provider package to enable OpenRouter integration with Mastra.

```bash
npm uninstall @ai-sdk/openai
npm install @openrouter/ai-sdk-provider
```

--------------------------------

### Equivalent Plugin Configuration for Web Search Shortcut (JSON)

Source: https://openrouter.ai/docs/guides/features/plugins/overview

This JSON example shows the explicit configuration using the 'plugins' array that achieves the same result as the ':online' model variant shortcut. It clarifies that model variants are a shorthand for standard plugin definitions, providing an alternative way to enable specific plugins like web search.

```json
{
  "model": "openai/gpt-4o",
  "plugins": [{ "id": "web" }]
}
```

--------------------------------

### Get total count of available models - TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/models

Retrieves the total count of available models from OpenRouter. This example demonstrates both the class-based method using the OpenRouter SDK instance and the standalone function approach using OpenRouterCore for better tree-shaking performance. Both methods require an API key from the environment.

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.models.count();

  console.log(result);
}

run();
```

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { modelsCount } from "@openrouter/sdk/funcs/modelsCount.js";

const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await modelsCount(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("modelsCount failed:", res.error);
  }
}

run();
```

--------------------------------

### SDK Implementation - C#

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

C# implementation using RestSharp to create an API key with proper request configuration.

```APIDOC
```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/keys");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Analytics Service Key\",\n  \"limit\": 150,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true,\n  \"expires_at\": \"2028-06-30T23:59:59Z\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```
```

--------------------------------

### Update Guardrail - JavaScript Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail

JavaScript implementation using the Fetch API to update a guardrail. Shows how to configure headers and handle the asynchronous response.

```APIDOC
### JavaScript Implementation

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000';
const options = {
  method: 'PATCH',
  headers: {
    'Authorization': 'Bearer <token>',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "name": "Updated Guardrail Name",
    "description": "Updated description",
    "limit_usd": 75,
    "reset_interval": "weekly"
  })
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

**Usage Notes:**
- Replace `<token>` with your actual Bearer token
- Use `JSON.stringify()` to convert the payload object to a string
- Always wrap the fetch call in a try-catch block for error handling
```

--------------------------------

### Fetch User Models from OpenRouter API

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-user

These examples demonstrate how to make an authenticated GET request to the OpenRouter API to retrieve a list of models associated with the current user. Each snippet uses a different programming language and its respective HTTP client library to send a request to the `/api/v1/models/user` endpoint. A valid API token, prefixed with 'Bearer', must be included in the Authorization header for successful authentication. The API will return a JSON object containing the user's model data.

```python
import requests

url = "https://openrouter.ai/api/v1/models/user"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/models/user';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/models/user"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/models/user")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models/user")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models/user', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/models/user");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models/user")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### GET /credits

Source: https://openrouter.ai/docs/sdks/python/api-reference/credits

Get total credits purchased and used for the authenticated user. A provisioning key is required for this operation.

```APIDOC
## GET /credits

### Description
Get total credits purchased and used for the authenticated user. A provisioning key is required for this operation.

### Method
GET

### Endpoint
/credits

### Response
#### Success Response (200)
- **Response Object** (operations.GetCreditsResponse) - Object containing details about total and used credits.
```

--------------------------------

### List Guardrails with OpenRouter TypeScript SDK Instance

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/guardrails

This TypeScript example demonstrates how to list all guardrails for the authenticated user using the main OpenRouter SDK instance. It initializes the SDK with an API key and then calls the `guardrails.list()` method. A provisioning API key is required for successful execution.

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.guardrails.list();

  console.log(result);
}

run();
```

--------------------------------

### GET /models

Source: https://openrouter.ai/docs/api/api-reference/models/get-models

Retrieves a list of all available models and their properties, with optional filtering by category or supported parameters.

```APIDOC
## GET /models

### Description
List all models and their properties.

### Method
GET

### Endpoint
/models

### Parameters
#### Header Parameters
- **Authorization** (string) - Required - API key as bearer token in Authorization header.

#### Query Parameters
- **category** (string, enum: programming, roleplay, marketing, marketing/seo, technology, science, translation, legal, finance, health, trivia, academia) - Optional - Filter models by use case category.
- **supported_parameters** (string) - Optional -
- **use_rss** (string) - Optional -
- **use_rss_chat_links** (string) - Optional -

### Response
#### Success Response (200)
- Returns a list of models or RSS feed.

#### Error Response (400)
- Bad Request - Invalid request parameters.

#### Error Response (500)
- Internal Server Error.
```

--------------------------------

### Install OpenRouter Python SDK

Source: https://openrouter.ai/docs/sdks/python/overview

Install the OpenRouter Python SDK using package managers (uv, pip, or poetry). Requires Python 3.9 or higher. The SDK is automatically generated from OpenAPI specifications.

```bash
# Using uv (recommended)
uv add openrouter

# Using pip
pip install openrouter

# Using poetry
poetry add openrouter
```

--------------------------------

### Import and Initialize OpenResponsesRequestProvider TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/openresponsesrequestprovider

Demonstrates how to import the OpenResponsesRequestProvider class from the OpenRouter SDK and create an instance. This is the basic setup required to specify routing preferences when multiple model providers are available.

```typescript
import { OpenResponsesRequestProvider } from "@openrouter/sdk/models";

let value: OpenResponsesRequestProvider = {};
```

--------------------------------

### GET /key

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key

Get information on the API key associated with the current authentication session. This endpoint provides details such as the key's label, usage, spending limits, and expiration.

```APIDOC
## GET /key

### Description
Get information on the API key associated with the current authentication session

### Method
GET

### Endpoint
/key

### Parameters
#### Path Parameters
_None_

#### Query Parameters
_None_

#### Request Body
_None_

#### Headers
- **Authorization** (string) - Required - API key as bearer token in Authorization header

### Request Example
```json
{}
```

### Response
#### Success Response (200)
- **data** (object) - API key details
  - **label** (string) - Required - Human-readable label for the API key
  - **limit** (number | null) - Required - Spending limit for the API key in USD
  - **usage** (number) - Required - Total OpenRouter credit usage (in USD) for the API key
  - **usage_daily** (number) - Required - OpenRouter credit usage (in USD) for the current UTC day
  - **usage_weekly** (number) - Required - OpenRouter credit usage (in USD) for the current UTC week (Monday-Sunday)
  - **usage_monthly** (number) - Required - OpenRouter credit usage (in USD) for the current UTC month
  - **byok_usage** (number) - Required - Total external BYOK usage (in USD) for the API key
  - **byok_usage_daily** (number) - Required - External BYOK usage (in USD) for the current UTC day
  - **byok_usage_weekly** (number) - Required - External BYOK usage (in USD) for the current UTC week (Monday-Sunday)
  - **byok_usage_monthly** (number) - Required - External BYOK usage (in USD) for current UTC month
  - **is_free_tier** (boolean) - Required - Whether this is a free tier API key
  - **is_management_key** (boolean) - Required - Whether this is a management key
  - **is_provisioning_key** (boolean) - Required - Whether this is a management key
  - **limit_remaining** (number | null) - Required - Remaining spending limit in USD
  - **limit_reset** (string | null) - Required - Type of limit reset for the API key
  - **include_byok_in_limit** (boolean) - Required - Whether to include external BYOK usage in the credit limit
  - **expires_at** (string | null) - ISO 8601 UTC timestamp when the API key expires, or null if no expiration
  - **rate_limit** (object) - Required - Legacy rate limit information about a key. Will always return -1.
    - **requests** (number) - Required - Number of requests allowed per interval
    - **interval** (string) - Required - Rate limit interval
    - **note** (string) - Required - Note about the rate limit

#### Error Response (401)
Unauthorized - Authentication required or invalid credentials

#### Error Response (500)
Internal Server Error - Unexpected server error

#### Response Example
```json
{
  "data": {
    "label": "My Main API Key",
    "limit": 100.0,
    "usage": 15.25,
    "usage_daily": 2.50,
    "usage_weekly": 7.75,
    "usage_monthly": 15.25,
    "byok_usage": 5.0,
    "byok_usage_daily": 1.0,
    "byok_usage_weekly": 3.0,
    "byok_usage_monthly": 5.0,
    "is_free_tier": false,
    "is_management_key": false,
    "is_provisioning_key": false,
    "limit_remaining": 84.75,
    "limit_reset": "monthly",
    "include_byok_in_limit": true,
    "expires_at": null,
    "rate_limit": {
      "requests": -1,
      "interval": "-1",
      "note": "Legacy rate limit information about a key. Will always return -1."
    }
  }
}
```
```

--------------------------------

### Install Claude Code via npm Package Manager

Source: https://openrouter.ai/docs/guides/guides/claude-code-integration

Install Claude Code globally using npm package manager. Requires Node.js 18 or newer to be installed on your system.

```bash
npm install -g @anthropic-ai/claude-code
```

--------------------------------

### Web Search Preview Tool Configuration

Source: https://openrouter.ai/docs/api/api-reference/responses/create-responses

Configures web search preview functionality with context size and user location parameters. Supports both standard and dated versions of the web search preview tool for flexible search capabilities.

```APIDOC
## Web Search Preview Tool

### Description
Configures web search preview tool with search context and user location information.

### Schema: OpenResponsesWebSearchPreviewTool

### Properties

#### type
- **Type**: OpenResponsesWebSearchPreviewToolType
- **Required**: Yes
- **Enum Values**: `web_search_preview`
- **Description**: Identifies this as a web search preview tool

#### search_context_size
- **Type**: ResponsesSearchContextSize
- **Required**: No
- **Enum Values**: `low`, `medium`, `high`
- **Description**: Size of search context to return with results

#### user_location
- **Type**: WebSearchPreviewToolUserLocation
- **Required**: No
- **Description**: User location information for localized search results

### User Location Properties

#### type
- **Type**: WebSearchPreviewToolUserLocationType
- **Required**: Yes
- **Enum Values**: `approximate`
- **Description**: Type of location specification

#### city
- **Type**: string | null
- **Required**: No
- **Description**: City name for location context

#### country
- **Type**: string | null
- **Required**: No
- **Description**: Country name for location context

#### region
- **Type**: string | null
- **Required**: No
- **Description**: Region or state for location context

#### timezone
- **Type**: string | null
- **Required**: No
- **Description**: Timezone identifier for location context

### Request Example
```json
{
  "type": "web_search_preview",
  "search_context_size": "high",
  "user_location": {
    "type": "approximate",
    "city": "San Francisco",
    "country": "United States",
    "region": "California",
    "timezone": "America/Los_Angeles"
  }
}
```
```

--------------------------------

### Define and Call Tools with OpenRouter AI API

Source: https://openrouter.ai/docs/api/reference/responses/tool-calling

This snippet demonstrates how to define a tool using the OpenAI function calling format and then make an API request to OpenRouter AI to utilize this tool. It covers setting up the tool definition, constructing the API request body with user input and tool information, and handling the API response. The examples show how to integrate tool-calling capabilities into AI interactions.

```typescript
const weatherTool = {
  type: 'function' as const,
  name: 'get_weather',
  description: 'Get the current weather in a location',
  strict: null,
  parameters: {
    type: 'object',
    properties: {
      location: {
        type: 'string',
        description: 'The city and state, e.g. San Francisco, CA',
      },
      unit: {
        type: 'string',
        enum: ['celsius', 'fahrenheit'],
      },
    },
    required: ['location'],
  },
};

const response = await fetch('https://openrouter.ai/api/v1/responses', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'openai/o4-mini',
    input: [
      {
        type: 'message',
        role: 'user',
        content: [
          {
            type: 'input_text',
            text: 'What is the weather in San Francisco?',
          },
        ],
      },
    ],
    tools: [weatherTool],
    tool_choice: 'auto',
    max_output_tokens: 9000,
  }),
});

const result = await response.json();
console.log(result);
```

```python
import requests

weather_tool = {
    'type': 'function',
    'name': 'get_weather',
    'description': 'Get the current weather in a location',
    'strict': None,
    'parameters': {
        'type': 'object',
        'properties': {
            'location': {
                'type': 'string',
                'description': 'The city and state, e.g. San Francisco, CA',
            },
            'unit': {
                'type': 'string',
                'enum': ['celsius', 'fahrenheit'],
            },
        },
        'required': ['location'],
    },
}

response = requests.post(
    'https://openrouter.ai/api/v1/responses',
    headers={
        'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
        'Content-Type': 'application/json',
    },
    json={
        'model': 'openai/o4-mini',
        'input': [
            {
                'type': 'message',
                'role': 'user',
                'content': [
                    {
                        'type': 'input_text',
                        'text': 'What is the weather in San Francisco?',
                    },
                ],
            },
        ],
        'tools': [weather_tool],
        'tool_choice': 'auto',
        'max_output_tokens': 9000,
    }
)

result = response.json()
print(result)
```

```bash
curl -X POST https://openrouter.ai/api/v1/responses \
  -H "Authorization: Bearer YOUR_OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/o4-mini",
    "input": [
      {
        "type": "message",
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "What is the weather in San Francisco?"
          }
        ]
      }
    ],
    "tools": [
      {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a location",
        "strict": null,
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    ],
    "tool_choice": "auto",
    "max_output_tokens": 9000
  }'
```

--------------------------------

### SDK Implementation - PHP

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

PHP implementation using Guzzle HTTP client to create an API key with authentication headers.

```APIDOC
```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/keys', [
  'body' => '{
  "name": "Analytics Service Key",
  "limit": 150,
  "limit_reset": "monthly",
  "include_byok_in_limit": true,
  "expires_at": "2028-06-30T23:59:59Z"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```
```

--------------------------------

### Best Practices for Descriptive Tool Names and Descriptions in JavaScript

Source: https://openrouter.ai/docs/sdks/call-model/tools

This JavaScript snippet illustrates the importance of providing clear and descriptive `name` and `description` for tools. It contrasts a 'good' example with a 'bad' one, emphasizing that detailed descriptions help the model understand the tool's purpose and improve its ability to use the tool effectively.

```javascript
// Good: Clear name and description
const tool1 = tool({
  name: 'search_knowledge_base',
  description: 'Search the company knowledge base for documents, FAQs, and policies. Returns relevant articles with snippets.',
  // ...
});

// Avoid: Vague or generic
const tool2 = tool({
  name: 'search',
  description: 'Searches stuff',
  // ...
});
```

--------------------------------

### Install TanStack AI with OpenRouter Adapter

Source: https://openrouter.ai/docs/guides/community/tanstack-ai

Install the required npm packages to use TanStack AI with OpenRouter. This includes the core TanStack AI library and the OpenRouter adapter package.

```bash
npm install @tanstack/ai @tanstack/ai-openrouter
```

--------------------------------

### TypeScript Example - Debug Chat Completions

Source: https://openrouter.ai/docs/api/reference/errors-and-debugging

Complete TypeScript example showing how to make a debug-enabled request to OpenRouter's Chat Completions API and parse the streaming response to display debug information.

```APIDOC
## TypeScript Implementation

### Description
TypeScript example for calling the Chat Completions API with debug mode enabled and processing the streaming response.

### Code
```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    Authorization: 'Bearer <OPENROUTER_API_KEY>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'anthropic/claude-haiku-4.5',
    stream: true,
    messages: [
      { role: 'system', content: 'You are a helpful assistant.' },
      { role: 'user', content: 'Hello!' },
    ],
    debug: {
      echo_upstream_body: true,
    },
  }),
});

const text = await response.text();

for (const line of text.split('\n')) {
  if (!line.startsWith('data: ')) continue;

  const data = line.slice(6);
  if (data === '[DONE]') break;

  const parsed = JSON.parse(data);

  if (parsed.debug?.echo_upstream_body) {
    console.log('\nDebug:', JSON.stringify(parsed.debug.echo_upstream_body, null, 2));
  }

  process.stdout.write(parsed.choices?.[0]?.delta?.content ?? '');
}
```

### Key Points
- Parse streaming response by splitting on newlines
- Filter lines starting with "data: " prefix
- Extract debug information from the first chunk
- Display transformed request body for inspection
- Continue processing remaining chunks for actual response content
```

--------------------------------

### Fetch Models Count via HTTP GET Request - C#

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

C# implementation using the RestSharp library to make a GET request to the OpenRouter API. Creates a REST client, configures the GET request with Bearer token authentication, and executes it.

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/models/count");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

--------------------------------

### Install OpenRouter DevTools as a development dependency (npm)

Source: https://openrouter.ai/docs/sdks/dev-tools/devtools

This command installs the OpenRouter DevTools package using npm, adding it as a development dependency to your project. The DevTools are strictly for development environments and will prevent accidental production deployment by throwing an error if `NODE_ENV` is set to 'production'.

```bash
npm install @openrouter/devtools --save-dev
```

--------------------------------

### Query OpenRouter Traces by Model Pattern

Source: https://openrouter.ai/docs/guides/features/broadcast/grafana

TraceQL query using regex pattern matching to find traces for models matching a specific pattern. This example finds all GPT-4 model variants using a wildcard regex.

```traceql
{ resource.service.name = "openrouter" && span.gen_ai.request.model =~ ".*gpt-4.*" }
```

--------------------------------

### Create a Guardrail using OpenRouter Python SDK

Source: https://openrouter.ai/docs/sdks/python/api-reference/guardrails

This example shows how to create a new guardrail for the authenticated user using the OpenRouter Python SDK. It initializes the client and then calls the `guardrails.create()` method, providing a name for the new guardrail. A provisioning key is required for this operation.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.create(name="My New Guardrail")

    # Handle response
    print(res)

```

--------------------------------

### Generate Context-Aware Instructions in OpenRouter SDK

Source: https://openrouter.ai/docs/sdks/typescript/call-model/dynamic-parameters

This snippet shows how to build dynamic `instructions` for the model based on the conversation's state. It incorporates the current turn number and can adapt the instruction's verbosity or content, for example, by asking for concise responses in longer conversations.

```typescript
const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  instructions: (ctx) => {
    const base = 'You are a helpful assistant.';
    const turnInfo = `This is turn ${ctx.numberOfTurns} of the conversation.`;

    // Add context based on history length
    if (ctx.numberOfTurns > 5) {
      return `${base}\n${turnInfo}\nKeep responses concise - this is a long conversation.`;
    }

    return `${base}\n${turnInfo}`;
  },
  input: 'Continue helping me...',
  tools: [helpTool],
});
```

--------------------------------

### Chat Completion with Google Gemini 3 Thinking Levels

Source: https://openrouter.ai/docs/best-practices/reasoning-tokens

Shows how to use Google Gemini 3 models with thinking levels via OpenRouter's reasoning.effort parameter. The example demonstrates mapping effort levels to Google's thinkingLevel API and extracting reasoning and content from the response. Requires OpenAI Python client with OpenRouter configuration.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="{{API_KEY_REF}}",
)

response = client.chat.completions.create(
    model="{{MODEL}}",
    messages=[
        {"role": "user", "content": "Explain the implications of quantum entanglement."}
    ],
    extra_body={
        "reasoning": {
            "effort": "low"
        }
    },
)

msg = response.choices[0].message
print(getattr(msg, "reasoning", None))
print(getattr(msg, "content", None))
```

--------------------------------

### Implement Chain-of-Thought Reasoning with Multiple AI Models (Python, TypeScript)

Source: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens

This advanced example demonstrates a chain-of-thought pattern where reasoning from one AI model is extracted and then injected as context into a prompt for a second AI model. This technique can improve the quality of responses by guiding the second model with a structured thought process. It involves making multiple API calls to different models.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="{{API_KEY_REF}}",
)

question = "Which is bigger: 9.11 or 9.9?"

def do_req(model: str, content: str, reasoning_config: dict | None = None):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "stop": "</think>",
    }
    if reasoning_config:
        payload.update(reasoning_config)
    return client.chat.completions.create(**payload)

# Get reasoning from a capable model
content = f"{question} Please think this through, but don't output an answer"
reasoning_response = do_req("deepseek/deepseek-r1", content)
reasoning = getattr(reasoning_response.choices[0].message, "reasoning", "")

# Let's test! Here's the naive response:
simple_response = do_req("openai/gpt-4o-mini", question)
print(getattr(simple_response.choices[0].message, "content", None))

# Here's the response with the reasoning token injected:
content = f"{question}. Here is some context to help you: {reasoning}"
smart_response = do_req("openai/gpt-4o-mini", content)
print(getattr(smart_response.choices[0].message, "content", None))
```

```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://openrouter.ai/api/v1',
  apiKey: '{{API_KEY_REF}}',
});

async function doReq(model, content, reasoningConfig) {
  const payload = {
    model,
    messages: [{ role: 'user', content }],
    stop: '</think>',
    ...reasoningConfig,
  };

  return openai.chat.completions.create(payload);
}

async function getResponseWithReasoning() {
  const question = 'Which is bigger: 9.11 or 9.9?';
  const reasoningResponse = await doReq(
    'deepseek/deepseek-r1',
    `${question} Please think this through, but don't output an answer`,
  );
  const reasoning = reasoningResponse.choices[0].message.reasoning;

  // Let's test! Here's the naive response:
  const simpleResponse = await doReq('openai/gpt-4o-mini', question);
  console.log(simpleResponse.choices[0].message.content);

  // Here's the response with the reasoning token injected:
  const content = `${question}. Here is some context to help you: ${reasoning}`;
  const smartResponse = await doReq('openai/gpt-4o-mini', content);
  console.log(smartResponse.choices[0].message.content);
}

getResponseWithReasoning();
```

--------------------------------

### Initialize OpenRouter, Load Environment, and Configure MCP Server in Python

Source: https://openrouter.ai/docs/guides/guides/mcp-servers

This Python code sets up the environment for interacting with OpenRouter and an MCP server. It loads API keys from a `.env` file, defines the LLM model to use, and configures the command and arguments for launching the File System MCP server. Dependencies include `asyncio`, `mcp`, `openai`, and `dotenv`.

```python
import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()  # load environment variables from .env

MODEL = "anthropic/claude-3-7-sonnet"

SERVER_CONFIG = {
    "command": "npx",
    "args": ["-y",
              "@modelcontextprotocol/server-filesystem",
              f"/Applications/"],
    "env": None
}
```

--------------------------------

### Import and Initialize PublicPricing TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/publicpricing

Import the PublicPricing type from the OpenRouter SDK and create a pricing object with prompt and completion rates. This example demonstrates the basic structure for defining model pricing information with required string fields for prompt and completion costs.

```typescript
import { PublicPricing } from "@openrouter/sdk/models";

let value: PublicPricing = {
  prompt: "0.00003",
  completion: "0.00006"
};
```

--------------------------------

### TypeScript Example - Chat Completion with Thinking Levels

Source: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens

TypeScript code example using the OpenAI client library to interact with Google Gemini 3 models via OpenRouter with reasoning effort levels. Shows proper type handling for the reasoning field in responses.

```APIDOC
## TypeScript Implementation Example

### Description
TypeScript example using OpenAI client library to create chat completions with Google Gemini 3 models and reasoning effort levels, with proper type definitions.

### Code
```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://openrouter.ai/api/v1',
  apiKey: 'YOUR_API_KEY',
});

async function getResponseWithThinkingLevel() {
  const response = await openai.chat.completions.create({
    model: 'google/gemini-3-pro-preview',
    messages: [
      {
        role: 'user',
        content: 'Explain the implications of quantum entanglement.',
      },
    ],
    reasoning: {
      effort: 'low', // Maps to thinkingLevel: "low"
    },
  });

  type ORChatMessage = (typeof response)['choices'][number]['message'] & {
    reasoning?: string;
  };
  const msg = response.choices[0].message as ORChatMessage;

  console.log('REASONING:', msg.reasoning);
  console.log('CONTENT:', msg.content);
}

getResponseWithThinkingLevel();
```

### Usage Notes
- Type extension allows proper TypeScript support for the reasoning field
- The reasoning field is optional and may not be present in all responses
- The effort level "low" provides moderate reasoning depth for balanced performance
```

--------------------------------

### GET /api/v1/guardrails/{id}

Source: https://openrouter.ai/docs/api/api-reference/guardrails/get-guardrail

Get a single guardrail by its unique ID. A management key is required for authentication to access this endpoint.

```APIDOC
## GET /api/v1/guardrails/{id}

### Description
Get a single guardrail by ID. A management key is required for authentication.

### Method
GET

### Endpoint
/api/v1/guardrails/{id}

### Parameters
#### Path Parameters
- **id** (string, uuid) - Required - The unique identifier of the guardrail to retrieve.

#### Header Parameters
- **Authorization** (string) - Required - API key as bearer token in Authorization header.

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
{}

### Response
#### Success Response (200)
- **data** (object) - The guardrail details.
  - **id** (string, uuid) - Unique identifier for the guardrail.
  - **name** (string) - Name of the guardrail.
  - **description** (string, null) - Description of the guardrail.
  - **limit_usd** (number, double, null) - Spending limit in USD.
  - **reset_interval** (string, null) - Interval at which the limit resets (daily, weekly, monthly).
  - **allowed_providers** (array of string, null) - List of allowed provider IDs.
  - **allowed_models** (array of string, null) - Array of model canonical_slugs (immutable identifiers).
  - **enforce_zdr** (boolean, null) - Whether to enforce zero data retention.
  - **created_at** (string) - ISO 8601 timestamp of when the guardrail was created.
  - **updated_at** (string, null) - ISO 8601 timestamp of when the guardrail was last updated.

#### Response Example
```json
{
  "data": {
    "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
    "name": "My Daily Spending Limit",
    "description": "Limits daily spending to $100",
    "limit_usd": 100.0,
    "reset_interval": "daily",
    "allowed_providers": [
      "openai",
      "anthropic"
    ],
    "allowed_models": [
      "gpt-4",
      "claude-3-opus"
    ],
    "enforce_zdr": true,
    "created_at": "2023-10-27T10:00:00Z",
    "updated_at": "2023-10-27T10:30:00Z"
  }
}
```
```

--------------------------------

### Install OpenRouter AI SDK Provider Package

Source: https://openrouter.ai/docs/community/vercel-ai-sdk

Install the @openrouter/ai-sdk-provider package using npm to enable OpenRouter integration with Vercel AI SDK. This is a prerequisite for using OpenRouter models in your Next.js application.

```bash
npm install @openrouter/ai-sdk-provider
```

--------------------------------

### Define a Basic Type-Safe Tool with OpenRouter SDK in TypeScript

Source: https://openrouter.ai/docs/sdks/call-model/tools

This example demonstrates how to create a basic tool using the `tool()` function from `@openrouter/sdk`. It defines the tool's name, description, input schema (for location), output schema (for temperature and conditions), and an asynchronous `execute` function to simulate fetching weather data.

```typescript
import { OpenRouter, tool } from '@openrouter/sdk';
import { z } from 'zod';

const weatherTool = tool({
  name: 'get_weather',
  description: 'Get the current weather for a location',
  inputSchema: z.object({
    location: z.string().describe('City name, e.g., "San Francisco, CA"')
  }),
  outputSchema: z.object({
    temperature: z.number(),
    conditions: z.string()
  }),
  execute: async (params) => {
    // params is typed as { location: string }
    const weather = await fetchWeather(params.location);
    return {
      temperature: weather.temp,
      conditions: weather.description
    };
  }
});
```

--------------------------------

### Send Audio File with OpenRouter TypeScript SDK

Source: https://openrouter.ai/docs/guides/overview/multimodal/audio

Complete example using the OpenRouter TypeScript SDK to send an audio file for transcription. Initializes the SDK with API credentials, encodes the audio file, and sends it with a text prompt to the specified model.

```typescript
import { OpenRouter } from '@openrouter/sdk';
import fs from "fs/promises";

const openRouter = new OpenRouter({
  apiKey: '{{API_KEY_REF}}',
});

async function encodeAudioToBase64(audioPath: string): Promise<string> {
  const audioBuffer = await fs.readFile(audioPath);
  return audioBuffer.toString("base64");
}

const audioPath = "path/to/your/audio.wav";
const base64Audio = await encodeAudioToBase64(audioPath);

const result = await openRouter.chat.send({
  model: "{{MODEL}}",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "Please transcribe this audio file.",
        },
        {
          type: "input_audio",
          inputAudio: {
            data: base64Audio,
            format: "wav",
          },
        },
      ],
    },
  ],
  stream: false,
});

console.log(result);
```

--------------------------------

### Send Chat Completion Request to OpenRouter API

Source: https://openrouter.ai/docs/app-attribution

Demonstrates how to send chat completion requests to the OpenRouter API using various programming languages and methods. Examples include using the dedicated OpenRouter SDK for TypeScript, the OpenAI SDK (adapted for OpenRouter) in Python and TypeScript, direct HTTP requests via `requests` (Python) and `fetch` (TypeScript), and a cURL command. All examples illustrate API key authentication, model selection, message formatting, and the inclusion of app attribution headers (`HTTP-Referer`, `X-Title`) for analytics and ranking.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': 'https://myapp.com', // Your app's URL
    'X-Title': 'My AI Assistant', // Your app's display name
  },
});

const completion = await openRouter.chat.send({
  model: 'openai/gpt-5.2',
  messages: [
    {
      role: 'user',
      content: 'Hello, world!',
    },
  ],
  stream: false,
});

console.log(completion.choices[0].message);
```

```python
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "https://myapp.com", # Your app's URL
    "X-Title": "My AI Assistant", # Your app's display name
  },
  model="openai/gpt-5.2",
  messages=[
    {
      "role": "user",
      "content": "Hello, world!"
    }
  ]
)
```

```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://openrouter.ai/api/v1',
  apiKey: '<OPENROUTER_API_KEY>',
  defaultHeaders: {
    'HTTP-Referer': 'https://myapp.com', // Your app's URL
    'X-Title': 'My AI Assistant', // Your app's display name
  },
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: 'openai/gpt-5.2',
    messages: [
      {
        role: 'user',
        content: 'Hello, world!',
      },
    ],
  });

  console.log(completion.choices[0].message);
}

main();
```

```python
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "HTTP-Referer": "https://myapp.com", # Your app's URL
    "X-Title": "My AI Assistant", # Your app's display name
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "openai/gpt-5.2",
    "messages": [
      {
        "role": "user",
        "content": "Hello, world!"
      }
    ]
  })
)
```

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    Authorization: 'Bearer <OPENROUTER_API_KEY>',
    'HTTP-Referer': 'https://myapp.com', // Your app's URL
    'X-Title': 'My AI Assistant', // Your app's display name
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'openai/gpt-5.2',
    messages: [
      {
        role: 'user',
        content: 'Hello, world!',
      },
    ],
  }),
});
```

```shell
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "HTTP-Referer: https://myapp.com" \
  -H "X-Title: My AI Assistant" \
  -d '{
  "model": "openai/gpt-5.2",
  "messages": [
    {
      "role": "user",
      "content": "Hello, world!"
    }
  ]
}'
```

--------------------------------

### Enable Fine-Grained Tool Streaming with Python Requests

Source: https://openrouter.ai/docs/guides/routing/provider-selection

Demonstrates how to enable fine-grained tool streaming using Python's requests library to make HTTP POST requests to OpenRouter API. Includes proper header configuration with beta feature flag and tool definition. Requires Bearer token authentication and requests library.

```python
import requests

headers = {
  'Authorization': 'Bearer <OPENROUTER_API_KEY>',
  'Content-Type': 'application/json',
  'x-anthropic-beta': 'fine-grained-tool-streaming-2025-05-14',
}

response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
  'model': 'anthropic/claude-sonnet-4.5',
  'messages': [{ 'role': 'user', 'content': 'What is the weather in Tokyo?' }],
  'tools': [
    {
      'type': 'function',
      'function': {
        'name': 'get_weather',
        'description': 'Get the current weather for a location',
        'parameters': {
          'type': 'object',
          'properties': {
            'location': { 'type': 'string' },
          },
          'required': ['location'],
        },
      },
    },
  ],
  'stream': True,
})
```

--------------------------------

### Fetch Models Count via HTTP GET Request - Swift

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

Swift implementation using Foundation's URLSession to make a GET request to the OpenRouter API. Constructs an HTTP request with Bearer token authentication and handles the response asynchronously.

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models/count")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### GET /api/v1/credits

Source: https://openrouter.ai/docs/api-reference/get-credits

Retrieve the total credits purchased and used for the authenticated user. A management key is required for authentication.

```APIDOC
## GET /api/v1/credits

### Description
Get total credits purchased and used for the authenticated user. Management key required.

### Method
GET

### Endpoint
/api/v1/credits

### Parameters
#### Path Parameters
- None

#### Query Parameters
- None

#### Request Body
- None

### Request Example
```
# Authentication is handled via the Authorization header (Bearer token).
# No request body is required for this GET endpoint.
```

### Response
#### Success Response (200)
- **data** (object) - An object containing the credit details.
  - **total_credits** (number) - The total credits purchased by the user.
  - **total_usage** (number) - The total credits used by the user.

#### Response Example
```json
{
  "data": {
    "total_credits": 100.5,
    "total_usage": 25.75
  }
}
```

### Errors
- **401 Unauthorized Error**: The authentication token is missing or invalid.
- **403 Forbidden Error**: The authenticated user does not have permission to access this resource.
- **500 Internal Server Error**: An unexpected error occurred on the server.
```

--------------------------------

### GET /models/count

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/models

Get the total count of available models.

```APIDOC
## GET /models/count

### Description
Get total count of available models

### Method
GET

### Endpoint
/models/count

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
{}

### Request Example
{}

### Response
#### Success Response (200)
- **count** (integer) - The total number of available models.

#### Response Example
{
  "count": 123
}

#### Error Response (500)
- **error** (string) - A description of the internal server error.

#### Error Response (4XX, 5XX)
- **error** (string) - A general error message.

#### Error Example
{
  "error": "Internal Server Error"
}
```

--------------------------------

### Find cheapest OpenRouter model by price with maximum latency

Source: https://openrouter.ai/docs/guides/routing/provider-selection

This code illustrates how to find the cheapest model from a list that adheres to a maximum acceptable latency (e.g., 3 seconds at p90). It utilizes `sort.by: 'price'`, `partition: 'none'`, and `preferredMaxLatency` within the `provider` options to prioritize cost-effective models that still meet latency constraints. This is useful for applications where response time is critical.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
});

const completion = await openRouter.chat.send({
  models: [
    'anthropic/claude-sonnet-4.5',
    'openai/gpt-5-mini',
  ],
  messages: [{ role: 'user', content: 'Hello' }],
  provider: {
    sort: {
      by: 'price',
      partition: 'none',
    },
    preferredMaxLatency: {
      p90: 3, // Prefer providers with <3 second latency for 90% of requests in last 5 minutes
    },
  },
  stream: false,
});
```

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer <OPENROUTER_API_KEY>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    models: [
      'anthropic/claude-sonnet-4.5',
      'openai/gpt-5-mini',
    ],
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      sort: {
        by: 'price',
        partition: 'none',
      },
      preferred_max_latency: {
        p90: 3, // Prefer providers with <3 second latency for 90% of requests in last 5 minutes
      },
    },
  }),
});
```

```python
import requests

headers = {
  'Authorization': 'Bearer <OPENROUTER_API_KEY>',
  'Content-Type': 'application/json',
}

response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
  'models': [

```

--------------------------------

### Fetch Models Count via HTTP GET Request - Go

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

Go implementation using the net/http package to make a GET request to the OpenRouter API. Constructs an HTTP request with Bearer token authentication, executes it, and reads the response body.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/models/count"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Set Model Behavior with System Instructions (TypeScript)

Source: https://openrouter.ai/docs/sdks/call-model/text-generation

This snippet shows how to guide the model's behavior and persona by providing system-level instructions using the `instructions` parameter in `callModel`.

```typescript
const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  instructions: 'You are a helpful coding assistant. Be concise and provide working code examples.',
  input: 'How do I read a file in Node.js?',
});
```

--------------------------------

### Fetch Models Count via HTTP GET Request - Java

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

Java implementation using the Unirest HTTP client library to make a GET request to the OpenRouter API. Includes Bearer token authentication header and returns the response as a string.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models/count")
  .header("Authorization", "Bearer <token>")
  .asString();
```

--------------------------------

### Send API Request to OpenRouter AI - Go

Source: https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages

Go example using the net/http package to send a POST request to OpenRouter AI's messages endpoint. Includes request creation, header configuration, and response body reading with proper resource cleanup.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/messages"

	payload := strings.NewReader("{\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"max_tokens\": 1024,\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"temperature\": 0.7\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Create OpenRouter LLM with Basic Configuration

Source: https://openrouter.ai/docs/guides/community/livekit

Initialize an OpenRouter LLM instance using the with_openrouter method within an AgentSession. This basic setup configures the Claude Sonnet model as the primary language model for the agent.

```python
from livekit.plugins import openai

session = AgentSession(
    llm=openai.LLM.with_openrouter(model="anthropic/claude-sonnet-4.5"),
    # ... tts, stt, vad, turn_detection, etc.
)
```

--------------------------------

### Example Chat Completion Response JSON

Source: https://openrouter.ai/docs/api-reference/chat-completion

This snippet provides an example of a successful JSON response from the OpenRouter API's chat completions endpoint. It includes details such as the generated message content, role, finish reason, potential tool calls, reasoning, and usage statistics for the request.

```json
{
  "id": "chatcmpl-7a1b2c3d4e5f67890123456789abcdef",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The theory of relativity, developed by Albert Einstein, explains how space and time are linked for objects moving at a consistent speed in a straight line. It shows that time can slow down or speed up depending on how fast you are moving relative to something else.",
        "name": "EinsteinBot",
        "tool_calls": [
          {
            "id": "toolcall-12345",
            "type": "function",
            "function": {
              "name": "fetch_relativity_summary",
              "arguments": "{\"topic\":\"theory of relativity\"}"
            }
          }
        ],
        "refusal": "",
        "reasoning": "The assistant provided a concise explanation suitable for a general audience.",
        "reasoning_details": [
          {
            "type": "reasoning.summary",
            "summary": "Simplified explanation of relativity theory for user query.",
            "id": "reasoning-001",
            "format": "openai-responses-v1",
            "index": 0
          }
        ],
        "images": [
          {
            "image_url": {
              "url": "https://openrouter.ai/assets/relativity_diagram.png"
            }
          }
        ]
      },
      "logprobs": {
        "content": [
          {
            "token": "The",
            "logprob": -0.01,
            "bytes": [
              84,
              104,
              101
            ],
            "top_logprobs": [
              {
                "token": "The",
                "logprob": -0.01,
                "bytes": [
                  84,
                  104,
                  101
                ]
              }
            ]
          }
        ],
        "refusal": [
          {
            "token": "",
            "logprob": 0,
            "bytes": [],
            "top_logprobs": [
              {
                "token": "",
                "logprob": 0,
                "bytes": []
              }
            ]
          }
        ]
      }
    }
  ],
  "created": 1712345678,
  "model": "openrouter-gpt-4",
  "object": "chat.completion",
  "system_fingerprint": "fingerprint-xyz-123",
  "usage": {
    "completion_tokens": 85,
    "prompt_tokens": 20,
    "total_tokens": 105,
    "completion_tokens_details": {
      "reasoning_tokens": 10,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 75,
      "rejected_prediction_tokens": 0
    },
    "prompt_tokens_details": {
      "cached_tokens": 15,
      "cache_write_tokens": 5,
      "audio_tokens": 0,
      "video_tokens": 0
    }
  }
}
```

--------------------------------

### GET /api/v1/keys

Source: https://openrouter.ai/docs/api/api-reference/api-keys/list

This endpoint allows an authenticated user to list all their API keys. A management key is required for this operation.

```APIDOC
## GET /api/v1/keys

### Description
List all API keys for the authenticated user. A management key is required for this operation.

### Method
GET

### Endpoint
/api/v1/keys

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
{}

### Response
#### Success Response (200)
- **data** (array of objects) - A list of API key objects.
- **data[].id** (string) - The unique identifier for the API key.
- **data[].name** (string) - The name or description of the API key.
- **data[].created_at** (string) - Timestamp when the API key was created (ISO 8601 format).
- **data[].last_used_at** (string, optional) - Timestamp when the API key was last used (ISO 8601 format). Null if never used.
- **data[].permissions** (array of strings) - Permissions associated with the API key (e.g., "read", "write").

#### Response Example
{
  "data": [
    {
      "id": "key_abc123",
      "name": "My Default Key",
      "created_at": "2023-01-01T12:00:00Z",
      "last_used_at": "2023-10-26T10:30:00Z",
      "permissions": [
        "read",
        "write"
      ]
    },
    {
      "id": "key_def456",
      "name": "Reporting Service Key",
      "created_at": "2023-02-15T09:00:00Z",
      "last_used_at": null,
      "permissions": [
        "read"
      ]
    }
  ]
}
```

--------------------------------

### GET /keys

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/apikeys

List all API keys for the authenticated user. Provisioning key required.

```APIDOC
## GET /keys

### Description
List all API keys for the authenticated user. Provisioning key required.

### Method
GET

### Endpoint
/keys

### Response
#### Success Response (200)
- **APIKeys** (array of object) - A list of API keys.
```

--------------------------------

### Fetch Models Count via HTTP GET Request - Ruby

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

Ruby implementation using the Net::HTTP library to make a GET request to the OpenRouter API. Establishes an HTTPS connection and includes Bearer token authentication in the request headers.

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/models/count")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

--------------------------------

### SDK Implementation - Python

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

Python implementation using the requests library to create an API key with rate limiting and expiration settings.

```APIDOC
```python
import requests

url = "https://openrouter.ai/api/v1/keys"

payload = {
    "name": "Analytics Service Key",
    "limit": 150,
    "limit_reset": "monthly",
    "include_byok_in_limit": True,
    "expires_at": "2028-06-30T23:59:59Z"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```
```

--------------------------------

### OpenAPI Specification for Get Credits Endpoint

Source: https://openrouter.ai/docs/api/api-reference/credits/get-credits

This YAML snippet defines the OpenAPI 3.1.1 specification for the `/credits` GET endpoint. It details the request parameters (Authorization header), expected responses (200, 401, 403, 500), and the schema for the successful response data, including total purchased and used credits.

```yaml
openapi: 3.1.1
info:
  title: Get remaining credits
  version: endpoint_credits.getCredits
paths:
  /credits:
    get:
      operationId: get-credits
      summary: Get remaining credits
      description: >-
        Get total credits purchased and used for the authenticated user.
        [Management key](/docs/guides/overview/auth/management-api-keys)
        required.
      tags:
        - - subpackage_credits
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the total credits purchased and used
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Credits_getCredits_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '403':
          description: Forbidden - Only management keys can fetch credits
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    CreditsGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        total_credits:
          type: number
          format: double
          description: Total credits purchased
        total_usage:
          type: number
          format: double
          description: Total credits used
      required:
        - total_credits
        - total_usage
    Credits_getCredits_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/CreditsGetResponsesContentApplicationJsonSchemaData
      required:
        - data
```

--------------------------------

### Create Skill Discovery Tool with TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

Defines a tool that lists all available skills with their descriptions and configuration status. The tool reads skill metadata from markdown files in a skills directory, filters by optional category, and returns structured skill information including name, description, and configuration availability.

```typescript
const skillDiscoveryTool = tool({
  name: 'list_skills',
  description: 'List all available skills with their descriptions',

  inputSchema: z.object({
    category: z.string().optional().describe('Filter by category'),
  }),

  outputSchema: z.object({
    skills: z.array(
      z.object({
        name: z.string(),
        description: z.string(),
        hasConfig: z.boolean(),
      })
    ),
    totalCount: z.number(),
  }),

  execute: async ({ category }) => {
    const availableSkills = listAvailableSkills();
    const skills = [];

    for (const skillName of availableSkills) {
      const skillPath = path.join(SKILLS_DIR, skillName, 'SKILL.md');
      const content = readFileSync(skillPath, 'utf-8');

      // Extract first paragraph as description
      const lines = content.split('\n').filter((l) => l.trim());
      const description = lines.find((l) => !l.startsWith('#')) || 'No description';

      // Check for config file
      const configPath = path.join(SKILLS_DIR, skillName, 'config.json');
      const hasConfig = existsSync(configPath);

      skills.push({
        name: skillName,
        description: description.slice(0, 100),
        hasConfig,
      });
    }

    return {
      skills,
      totalCount: skills.length,
    };
  },
});
```

--------------------------------

### GET /api/v1/credits

Source: https://openrouter.ai/docs/api/api-reference/credits/get-credits

This endpoint allows an authenticated user to retrieve their total purchased and used credits. A management API key is required for access.

```APIDOC
## GET /api/v1/credits

### Description
Get total credits purchased and used for the authenticated user. A management key is required for authentication.

### Method
GET

### Endpoint
https://openrouter.ai/api/v1/credits

### Parameters
#### Header Parameters
- **Authorization** (string) - Required - API key as bearer token (e.g., `Bearer <token>`).

#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(None)

### Response
#### Success Response (200)
- **data** (object) - Contains credit usage details.
  - **total_credits** (number) - Total credits purchased by the user.
  - **total_usage** (number) - Total credits used by the user.

#### Response Example
{
  "data": {
    "total_credits": 123.45,
    "total_usage": 67.89
  }
}
```

--------------------------------

### Call Model with Skills Tool

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

Demonstrates how to invoke the OpenRouter model with the skills tool enabled. The model will automatically call the Skill tool to load context, and subsequent responses will have access to the skill's instructions.

```typescript
const result = openrouter.callModel({
  model: 'anthropic/claude-sonnet-4.5',
  input: 'I need to process a PDF and extract tables from it',
  tools: [skillsTool],
});

const text = await result.getText();
// The model will call the Skill tool, loading pdf-processing context
// Subsequent responses will have access to the skill's instructions
```

--------------------------------

### Initialize OpenRouter SDK and Generate Text (TypeScript)

Source: https://openrouter.ai/docs/sdks/call-model/text-generation

This snippet demonstrates the basic initialization of the OpenRouter SDK with an API key and how to make a simple text generation call using `callModel` with a string input, then retrieve the text output.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openrouter = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  input: 'Explain quantum computing in one sentence.',
});

const text = await result.getText();
```

--------------------------------

### Configure Provider Sorting and Latency Preferences - cURL

Source: https://openrouter.ai/docs/guides/routing/provider-selection

Set up OpenRouter API request using cURL with model selection, provider sorting by price, and preferred maximum latency constraints. This example demonstrates basic provider configuration with a single p90 latency percentile cutoff of 3 seconds.

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer <OPENROUTER_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "models": [
      "anthropic/claude-sonnet-4.5",
      "openai/gpt-5-mini"
    ],
    "messages": [{ "role": "user", "content": "Hello" }],
    "provider": {
      "sort": {
        "by": "price",
        "partition": "none"
      },
      "preferred_max_latency": {
        "p90": 3
      }
    }
  }'
```

--------------------------------

### GET /models

Source: https://openrouter.ai/docs/api/api-reference/embeddings/list-embeddings-models

Retrieves a list of all available AI models with their complete specifications including pricing, capabilities, and supported parameters. This endpoint returns detailed information about each model's architecture, context length, and default parameters.

```APIDOC
## GET /models

### Description
Retrieve a comprehensive list of all available AI models with detailed specifications including pricing, capabilities, supported parameters, and provider information.

### Method
GET

### Endpoint
/models

### Response
#### Success Response (200)
- **data** (array) - Array of Model objects containing complete model information

#### Model Object Properties
- **id** (string) - Required - Unique identifier for the model
- **canonical_slug** (string) - Required - Canonical slug for the model
- **hugging_face_id** (string, null) - Optional - Hugging Face model identifier
- **name** (string) - Required - Display name of the model
- **created** (number) - Required - Unix timestamp of model creation
- **description** (string) - Required - Description of the model
- **pricing** (PublicPricing) - Required - Pricing information for the model
- **context_length** (number, null) - Required - Maximum context length in tokens
- **architecture** (ModelArchitecture) - Required - Model architecture details
- **top_provider** (TopProviderInfo) - Required - Information about the top provider
- **per_request_limits** (PerRequestLimits) - Required - Per-request token limits
- **supported_parameters** (array) - Required - List of supported parameters
- **default_parameters** (DefaultParameters) - Required - Default parameter values
- **expiration_date** (string, null) - Optional - ISO 8601 expiration date or null

#### TopProviderInfo Object
- **context_length** (number, null) - Context length from the top provider
- **max_completion_tokens** (number, null) - Maximum completion tokens from the top provider
- **is_moderated** (boolean) - Required - Whether the top provider moderates content

#### PerRequestLimits Object
- **prompt_tokens** (number) - Required - Maximum prompt tokens per request
- **completion_tokens** (number) - Required - Maximum completion tokens per request

#### DefaultParameters Object
- **temperature** (number, null) - Optional - Default temperature value
- **top_p** (number, null) - Optional - Default top_p value
- **frequency_penalty** (number, null) - Optional - Default frequency penalty value

#### Supported Parameters
Models may support the following parameters:
- temperature
- top_p
- top_k
- min_p
- top_a
- frequency_penalty
- presence_penalty
- repetition_penalty
- max_tokens
- logit_bias
- logprobs
- top_logprobs
- seed
- response_format
- structured_outputs
- stop
- tools
- tool_choice
- parallel_tool_calls
- include_reasoning
- reasoning
- reasoning_effort
- web_search_options
- verbosity

#### Response Example
{
  "data": [
    {
      "id": "model-id-123",
      "canonical_slug": "model-name",
      "hugging_face_id": "org/model-name",
      "name": "Model Display Name",
      "created": 1609459200,
      "description": "A description of the model",
      "pricing": {
        "prompt": 0.000005,
        "completion": 0.000015
      },
      "context_length": 4096,
      "architecture": {
        "modality": "text",
        "input_modalities": ["text"],
        "output_modalities": ["text"]
      },
      "top_provider": {
        "context_length": 4096,
        "max_completion_tokens": 2048,
        "is_moderated": false
      },
      "per_request_limits": {
        "prompt_tokens": 4000,
        "completion_tokens": 2000
      },
      "supported_parameters": ["temperature", "top_p", "max_tokens"],
      "default_parameters": {
        "temperature": 0.7,
        "top_p": 1.0,
        "frequency_penalty": null
      },
      "expiration_date": null
    }
  ]
}
```

--------------------------------

### Make OpenRouter AI API Tool Call Request

Source: https://openrouter.ai/docs/api/api-reference/responses/create-responses

These examples demonstrate how to make a POST request to the OpenRouter AI API to send a user message and define a tool (function call) for external interaction, such as fetching weather data. Each example includes setting required authorization and content-type headers, and sending a JSON payload with the message and tool definitions. This allows the AI model to understand and potentially invoke external functions based on user input.

```php
<?php

$client = new GuzzleHttp\Client();
$response = $client->request('POST', 'https://openrouter.ai/api/v1/responses', [
  'body' => '{
  "input": [
    {
      "type": "message",
      "role": "user",
      "content": "Hello, how are you?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string"
          }
        }
      }
    }
  ],
  "model": "anthropic/claude-4.5-sonnet-20250929",
  "temperature": 0.7,
  "top_p": 0.9
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/responses");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "input": [
    [
      "type": "message",
      "role": "user",
      "content": "Hello, how are you?"
    ]
  ],
  "tools": [
    [
      "type": "function",
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": [
        "type": "object",
        "properties": ["location": ["type": "string"]]
      ]
    ]
  ],
  "model": "anthropic/claude-4.5-sonnet-20250929",
  "temperature": 0.7,
  "top_p": 0.9
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/responses")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Example Server-Sent Event for Mid-Stream Error

Source: https://openrouter.ai/docs/api/reference/errors-and-debugging

This example demonstrates the format of a Server-Sent Event (SSE) containing a mid-stream error. It shows how the error details are embedded within the `data` field, conforming to the `MidStreamError` type, and indicates a provider disconnection.

```text
data: {"id":"cmpl-abc123","object":"chat.completion.chunk","created":1234567890,"model":"gpt-3.5-turbo","provider":"openai","error":{"code":"server_error","message":"Provider disconnected"},"choices":[{"index":0,"delta":{"content":""},"finish_reason":"error"}]}
```

--------------------------------

### GET /keys

Source: https://openrouter.ai/docs/api/api-reference/api-keys/list

This endpoint allows users to retrieve a list of all API keys associated with their authenticated account. A management key is required for this operation.

```APIDOC
## GET /keys

### Description
List all API keys for the authenticated user. A management key is required.

### Method
GET

### Endpoint
/keys

### Parameters
#### Query Parameters
- **include_disabled** (string) - Optional - Whether to include disabled API keys in the response
- **offset** (string) - Optional - Number of API keys to skip for pagination

#### Headers
- **Authorization** (string) - Required - API key as bearer token in Authorization header

### Request Example
```json
{}
```

### Response
#### Success Response (200)
- **data** (array) - List of API keys
  - **hash** (string) - Unique hash identifier for the API key
  - **name** (string) - Name of the API key
  - **label** (string) - Human-readable label for the API key
  - **disabled** (boolean) - Whether the API key is disabled
  - **limit** (number/null) - Spending limit for the API key in USD
  - **limit_remaining** (number/null) - Remaining spending limit in USD
  - **limit_reset** (string/null) - Type of limit reset for the API key
  - **include_byok_in_limit** (boolean) - Whether to include external BYOK usage in the credit limit
  - **usage** (number) - Total OpenRouter credit usage (in USD) for the API key
  - **usage_daily** (number) - OpenRouter credit usage (in USD) for the current UTC day
  - **usage_weekly** (number) - OpenRouter credit usage (in USD) for the current UTC week (Monday-Sunday)
  - **usage_monthly** (number) - OpenRouter credit usage (in USD) for the current UTC month
  - **byok_usage** (number) - Total external BYOK usage (in USD) for the API key
  - **byok_usage_daily** (number) - External BYOK usage (in USD) for the current UTC day
  - **byok_usage_weekly** (number) - External BYOK usage (in USD) for the current UTC week (Monday-Sunday)
  - **byok_usage_monthly** (number) - External BYOK usage (in USD) for current UTC month
  - **created_at** (string) - ISO 8601 timestamp of when the API key was created
  - **updated_at** (string/null) - ISO 8601 timestamp of when the API key was last updated
  - **expires_at** (string/null) - ISO 8601 UTC timestamp when the API key expires, or null if no expiration

#### Response Example
```json
{
  "data": [
    {
      "hash": "key_hash_example_1",
      "name": "My Development Key",
      "label": "Dev Environment",
      "disabled": false,
      "limit": 100.0,
      "limit_remaining": 75.5,
      "limit_reset": "monthly",
      "include_byok_in_limit": true,
      "usage": 24.5,
      "usage_daily": 1.2,
      "usage_weekly": 5.0,
      "usage_monthly": 24.5,
      "byok_usage": 10.0,
      "byok_usage_daily": 0.5,
      "byok_usage_weekly": 2.0,
      "byok_usage_monthly": 10.0,
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-15T10:30:00Z",
      "expires_at": null
    },
    {
      "hash": "key_hash_example_2",
      "name": "Production Key",
      "label": "Prod Service A",
      "disabled": false,
      "limit": 500.0,
      "limit_remaining": 480.0,
      "limit_reset": "weekly",
      "include_byok_in_limit": false,
      "usage": 20.0,
      "usage_daily": 5.0,
      "usage_weekly": 20.0,
      "usage_monthly": 80.0,
      "byok_usage": 0.0,
      "byok_usage_daily": 0.0,
      "byok_usage_weekly": 0.0,
      "byok_usage_monthly": 0.0,
      "created_at": "2023-02-10T08:00:00Z",
      "updated_at": null,
      "expires_at": "2024-02-10T08:00:00Z"
    }
  ]
}
```
```

--------------------------------

### Specify OpenRouter Presets using the 'preset' Field

Source: https://openrouter.ai/docs/guides/features/presets

This example illustrates how to apply an OpenRouter preset using the dedicated 'preset' field, while also specifying a base 'model'. The preset's configurations will be shallow-merged with the explicitly provided model and other request parameters.

```json
{
  "model": "openai/gpt-4",
  "preset": "email-copywriter",
  "messages": [
    {
      "role": "user",
      "content": "Write a marketing email about our new feature"
    }
  ]
}
```

--------------------------------

### POST /api/v1/chat/completions - Sampling Parameters

Source: https://openrouter.ai/docs/api/reference/parameters

This documentation describes the various sampling parameters that can be included in the request body when making a chat completion request to the OpenRouter API. These parameters control the model's token generation process, influencing creativity, predictability, and repetition. Please note that the endpoint and request/response examples are illustrative, based on common LLM API patterns, as the source text primarily focuses on parameter descriptions.

```APIDOC
## POST /api/v1/chat/completions

### Description
This endpoint facilitates sending messages to an AI model to receive a chat completion. The parameters detailed below are specifically designed to fine-tune the model's token generation behavior, influencing aspects like creativity, predictability, and repetition. Please note that the endpoint and request/response examples are illustrative, based on common LLM API patterns, as the source text primarily focuses on parameter descriptions.

### Method
POST

### Endpoint
/api/v1/chat/completions

### Parameters
#### Request Body
- **model** (string) - Required - The ID of the model to use for the completion. (Illustrative)
- **messages** (array of objects) - Required - A list of messages comprising the conversation so far. (Illustrative)
  - **role** (string) - Required - The role of the author of this message (e.g., "user", "assistant", "system").
  - **content** (string) - Required - The content of the message.
- **temperature** (float) - Optional - Range: 0.0 to 2.0. Default: 1.0. Influences the variety in the model's responses. Lower values lead to more predictable and typical responses, while higher values encourage more diverse and less common responses. At 0, the model always gives the same response for a given input.
- **top_p** (float) - Optional - Range: 0.0 to 1.0. Default: 1.0. Limits the model's choices to a percentage of likely tokens: only the top tokens whose probabilities add up to P. A lower value makes the model's responses more predictable, while the default setting allows for a full range of token choices.
- **top_k** (integer) - Optional - Range: 0 or above. Default: 0. Limits the model's choice of tokens at each step, making it choose from a smaller set. A value of 1 means the model will always pick the most likely next token, leading to predictable results. By default this setting is disabled, making the model to consider all choices.
- **frequency_penalty** (float) - Optional - Range: -2.0 to 2.0. Default: 0.0. Aims to control the repetition of tokens based on how often they appear in the input. It tries to use less frequently those tokens that appear more in the input, proportional to how frequently they occur. Token penalty scales with the number of occurrences. Negative values will encourage token reuse.
- **presence_penalty** (float) - Optional - Range: -2.0 to 2.0. Default: 0.0. Adjusts how often the model repeats specific tokens already used in the input. Higher values make such repetition less likely, while negative values do the opposite. Token penalty does not scale with the number of occurrences. Negative values will encourage token reuse.
- **repetition_penalty** (float) - Optional - Range: 0.0 to 2.0. Default: 1.0. Helps to reduce the repetition of tokens from the input. A higher value makes the model less likely to repeat tokens, but too high a value can make the output less coherent (often with run-on sentences that lack small words). Token penalty scales based on original token's probability.
- **min_p** (float) - Optional - Range: 0.0 to 1.0. Default: 0.0. Represents the minimum probability for a token to be considered, relative to the probability of the most likely token. If your Min-P is set to 0.1, that means it will only allow for tokens that are at least 1/10th as probable as the best possible option.

### Request Example
```json
{
  "model": "openrouter/auto",
  "messages": [
    { "role": "user", "content": "Tell me a short story about a brave knight." }
  ],
  "temperature": 0.7,
  "top_p": 0.9,
  "max_tokens": 150,
  "frequency_penalty": 0.5
}
```

### Response
#### Success Response (200)
- **id** (string) - Unique identifier for the chat completion.
- **object** (string) - The type of object, typically "chat.completion".
- **created** (integer) - Unix timestamp (in seconds) of when the completion was created.
- **model** (string) - The model ID used for the completion.
- **choices** (array) - A list of chat completion choices.
  - **index** (integer) - The index of the choice in the list.
  - **message** (object) - The generated message.
    - **role** (string) - The role of the author of this message (e.g., "assistant").
    - **content** (string) - The content of the message.
  - **finish_reason** (string) - The reason the model stopped generating tokens (e.g., "stop", "length").
- **usage** (object) - Information about the API request's token usage.
  - **prompt_tokens** (integer) - The number of tokens in the prompt.
  - **completion_tokens** (integer) - The number of tokens in the completion.
  - **total_tokens** (integer) - The total number of tokens used in the request (prompt + completion).

#### Response Example
```json
{
  "id": "chatcmpl-8f3b2e7c-1d4a-4e5f-8c9d-0a1b2c3d4e5f",
  "object": "chat.completion",
  "created": 1701388800,
  "model": "openrouter/auto",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Sir Reginald, a knight of unwavering courage, stood before the dragon's lair. His shield bore the crest of a roaring lion, and his sword, 'Truthspeaker,' gleamed in the dim light. With a deep breath, he stepped into the darkness, ready to face his destiny."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 60,
    "total_tokens": 75
  }
}
```
```

--------------------------------

### Import and instantiate GetCurrentKeyResponse - TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getcurrentkeyresponse

Demonstrates how to import the GetCurrentKeyResponse type from the OpenRouter SDK and create an instance with API key details including usage metrics, limits, and rate limiting information. This example shows the complete structure of the response object with all available fields populated.

```typescript
import { GetCurrentKeyResponse } from "@openrouter/sdk/models/operations";

let value: GetCurrentKeyResponse = {
  data: {
    label: "sk-or-v1-au7...890",
    limit: 100,
    usage: 25.5,
    usageDaily: 25.5,
    usageWeekly: 25.5,
    usageMonthly: 25.5,
    byokUsage: 17.38,
    byokUsageDaily: 17.38,
    byokUsageWeekly: 17.38,
    byokUsageMonthly: 17.38,
    isFreeTier: false,
    isProvisioningKey: false,
    limitRemaining: 74.5,
    limitReset: "monthly",
    includeByokInLimit: false,
    rateLimit: {
      requests: 1000,
      interval: "1h",
      note: "This field is deprecated and safe to ignore."
    }
  }
};
```

--------------------------------

### Example JSON Response for List Endpoints Data

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listendpointsresponse

This JSON object provides an example of the `data` field's structure, illustrating the response for listing available endpoints for a model. It includes details such as model ID, name, description, architecture, and a list of endpoints with their pricing, provider, and performance metrics.

```json
{
  "id": "openai/gpt-4",
  "name": "GPT-4",
  "created": 1692901234,
  "description": "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy.",
  "architecture": {
    "tokenizer": "GPT",
    "instruct_type": "chatml",
    "modality": "text->text",
    "input_modalities": [
      "text"
    ],
    "output_modalities": [
      "text"
    ]
  },
  "endpoints": [
    {
      "name": "OpenAI: GPT-4",
      "model_name": "GPT-4",
      "context_length": 8192,
      "pricing": {
        "prompt": "0.00003",
        "completion": "0.00006",
        "request": "0",
        "image": "0"
      },
      "provider_name": "OpenAI",
      "tag": "openai",
      "quantization": "fp16",
      "max_completion_tokens": 4096,
      "max_prompt_tokens": 8192,
      "supported_parameters": [
        "temperature",
        "top_p",
        "max_tokens",
        "frequency_penalty",
        "presence_penalty"
      ],
      "status": "default",
      "uptime_last_30m": 99.5,
      "supports_implicit_caching": true,
      "latency_last_30m": {
        "p50": 0.25,
        "p75": 0.35,
        "p90": 0.48,
        "p99": 0.85
      },
      "throughput_last_30m": {
        "p50": 45.2,
        "p75": 38.5,
        "p90": 28.3,
        "p99": 15.1
      }
    }
  ]
}
```

--------------------------------

### List Guardrails using OpenRouter Python SDK

Source: https://openrouter.ai/docs/sdks/python/api-reference/guardrails

This example demonstrates how to list all guardrails associated with the authenticated user using the OpenRouter Python SDK. It initializes the client with an API key from an environment variable and then calls the `guardrails.list()` method. A provisioning key is required for this operation.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.list()

    # Handle response
    print(res)

```

--------------------------------

### Enable Web Search for Free OpenRouter Models

Source: https://openrouter.ai/docs/guides/features/plugins/web-search

This example illustrates how to apply the `:online` web search shortcut to free model variants on OpenRouter. While enabling web search for free models, it's important to note that this feature will still incur additional costs. This allows users to leverage web grounding even with cost-effective models.

```json
{
  "model": "openai/gpt-oss-20b:free:online"
}
```

--------------------------------

### Generate Text with String Input using callModel (TypeScript)

Source: https://openrouter.ai/docs/sdks/call-model/text-generation

This example shows how to use a simple string as input for the `callModel` function to generate a response from the specified model.

```typescript
const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  input: 'What is the speed of light?',
});
```

--------------------------------

### Retrieve a Single API Key with OpenRouter SDK (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/apikeys

This TypeScript example demonstrates how to fetch a single API key using the main OpenRouter SDK. It initializes the SDK with an API key, then calls the `apiKeys.get` method, passing the key's hash as a parameter. The result is logged to the console.

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.apiKeys.get({
    hash: "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943",
  });

  console.log(result);
}

run();
```

--------------------------------

### Example of Actionable Error Message (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/overview

This snippet provides an example of the actionable error messages generated by the SDK. It demonstrates how the SDK offers specific guidance for common issues, such as insufficient messages for a model, rather than generic error codes, aiding in faster debugging.

```typescript
// Instead of generic errors, get specific guidance:
// "Model 'openai/o1-preview' requires at least 2 messages.
//  You provided 1 message. Add a system or user message."
```

--------------------------------

### Broadcast Configuration and Setup

Source: https://openrouter.ai/docs/guides/features/broadcast

Configure broadcast settings to enable automatic trace sending to external observability platforms. Manage destinations, credentials, and trace enrichment options.

```APIDOC
## Broadcast Configuration

### Description
Configure broadcast settings to automatically send traces from OpenRouter API requests to external observability and analytics platforms.

### Enabling Broadcast
1. Navigate to Settings > Observability in OpenRouter dashboard
2. Toggle the "Enable Broadcast" switch to turn on the feature
3. Add one or more destinations where traces will be sent

### Requirements
- Must be an organization admin to edit broadcast settings for organization accounts
- Each destination requires specific configuration (API keys, endpoints, project identifiers)
- Credentials are encrypted and stored securely

### Trace Enrichment Options

#### User ID Field
- **Field Name**: `user`
- **Type**: string
- **Max Length**: 128 characters
- **Purpose**: Associate traces with specific end-users to track usage patterns and debug issues

#### Session ID Field
- **Field Name**: `session_id`
- **Type**: string
- **Max Length**: 128 characters
- **Alternative**: Can also be passed via `x-session-id` HTTP header
- **Purpose**: Group related requests together (conversations, agent workflows)

#### Custom Metadata
- **Field Name**: `trace`
- **Type**: JSON object
- **Purpose**: Pass arbitrary metadata for advanced observability workflows
- **Flexibility**: Accepts any key-value pairs; certain keys have special meaning per destination

### Available Destinations

#### Currently Supported
- Arize AI
- Braintrust
- ClickHouse
- Comet Opik
- Datadog
- Grafana Cloud
- Langfuse
- LangSmith
- New Relic
- OpenTelemetry Collector
- PostHog
- S3 / S3-Compatible
- Sentry
- Snowflake
- W&B Weave
- Webhook

#### Coming Soon
- AWS Firehose
- Dynatrace
- Evidently
- Fiddler
- Galileo
- Helicone
- HoneyHive
- Keywords AI
- Middleware
- Mona
- OpenInference
- Phoenix
- Portkey
- Supabase
- WhyLabs

### Trace Data Included in Broadcasts
- Request and response data (input messages and model output)
- Token usage (prompt, completion, and total tokens)
- Cost information (total request cost)
- Timing metrics (start time, end time, latency)
- Model information (model slug and provider name)
- Tool usage (tools included and tool calls made)
```

--------------------------------

### Call Model with System Instructions - TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/call-model/overview

Makes an LLM call with system instructions to guide the model's behavior. System instructions define the assistant's role and behavior for the conversation.

```typescript
// With system instructions
const result3 = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  instructions: 'You are a helpful assistant.',
  input: 'Hello!',
});
```

--------------------------------

### GET /guardrails/{id} - Get Guardrail

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/guardrails

Retrieve details of a specific guardrail by its ID. Returns comprehensive information about the guardrail configuration and settings.

```APIDOC
## GET /guardrails/{id}

### Description
Get a specific guardrail by ID.

### Method
GET

### Endpoint
/guardrails/{id}

### Parameters
#### Path Parameters
- **id** (string) - Required - Unique identifier of the guardrail

### Response
#### Success Response (200)
- **id** (string) - Unique identifier for the guardrail
- **name** (string) - Name of the guardrail
- **description** (string) - Description of the guardrail
- **config** (object) - Guardrail configuration settings
- **created_at** (string) - ISO 8601 timestamp of creation
- **updated_at** (string) - ISO 8601 timestamp of last update
```

--------------------------------

### Utilize Multiple AI Models with OpenRouter Agents in TypeScript

Source: https://openrouter.ai/docs/community/mastra

This example demonstrates how to initialize the OpenRouter provider once and then create multiple `Agent` instances, each configured with a different model available through OpenRouter (e.g., Claude and GPT-4). It shows how to generate responses from these distinct agents, allowing for flexible model selection based on task requirements.

```typescript
import { Agent } from '@mastra/core/agent';
import { createOpenRouter } from '@openrouter/ai-sdk-provider';

const openrouter = createOpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

// Create agents using different models
const claudeAgent = new Agent({
  model: openrouter('anthropic/claude-3-opus'),
  name: 'ClaudeAssistant',
  instructions: 'You are a helpful assistant powered by Claude.',
});

const gptAgent = new Agent({
  model: openrouter('openai/gpt-4'),
  name: 'GPTAssistant',
  instructions: 'You are a helpful assistant powered by GPT-4.',
});

// Use different agents based on your needs
const claudeResponse = await claudeAgent.generate([
  {
    role: 'user',
    content: 'Explain quantum mechanics simply.',
  },
]);
console.log(claudeResponse.text);

const gptResponse = await gptAgent.generate([
  {
    role: 'user',
    content: 'Explain quantum mechanics simply.',
  },
]);
console.log(gptResponse.text);
```

--------------------------------

### GET /models/count

Source: https://openrouter.ai/docs/sdks/python/api-reference/models/models

Get the total count of available models in the OpenRouter API. This endpoint returns the number of models currently available for use.

```APIDOC
## GET /models/count

### Description
Get total count of available models

### Method
GET

### Endpoint
/models/count

### Parameters
#### Query Parameters
- **retries** (Optional[utils.RetryConfig]) - Optional - Configuration to override the default retry behavior of the client.

### Request Example
```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:
    res = open_router.models.count()
    print(res)
```

### Response
#### Success Response (200)
- **ModelsCountResponse** (components.ModelsCountResponse) - Response containing the total count of available models

### Error Handling
| Error Type | Status Code | Content Type |
| --- | --- | --- |
| InternalServerResponseError | 500 | application/json |
| OpenRouterDefaultError | 4XX, 5XX | */* |
```

--------------------------------

### Get Generation Response Object Structure

Source: https://openrouter.ai/docs/sdks/python/api-reference/operations/getgenerationresponse

This section describes the structure of the response object returned when retrieving a generation from the OpenRouter API via the Python SDK. The exact API endpoint is not explicitly provided in the source text but is inferred as a GET operation.

```APIDOC
## GET /generations/{id} (Inferred Endpoint)

### Description
This describes the data structure of the response received after a generation request. It is typically returned by an SDK method like `GetGenerationResponse`.

### Method
GET (Inferred from "GetGenerationResponse" method name)

### Endpoint
/generations/{id} (Inferred, as not explicitly stated in the source text. `{id}` would be the identifier for the generation.)

### Parameters
#### Path Parameters
- **id** (string) - Required - The unique identifier of the generation. (Inferred)

#### Query Parameters
(None explicitly mentioned in the source text for this response structure)

#### Request Body
(Not applicable for a GET request to retrieve a specific resource)

### Request Example
(No explicit request example provided in the source text, as this document focuses on the response structure. A typical request would involve calling an SDK method like `client.get_generation_response(id="gen_abc123")`.)

### Response
#### Success Response (200 OK)
- **data** ([operations.GetGenerationData](/docs/sdks/operations/operations/getgenerationdata)) - Required - Generation data. This field contains the core details of the generated content.

#### Response Example
{
  "data": {
    // Structure of operations.GetGenerationData
    // Example:
    "id": "gen_example_123",
    "status": "completed",
    "output": {
      "text": "This is an example of the generated text content."
    }
  }
}
```

--------------------------------

### GET /api/v1/keys/{key_hash}

Source: https://openrouter.ai/docs/guides/overview/auth/management-api-keys

Retrieve details for a specific API key by its hash identifier.

```APIDOC
## GET /api/v1/keys/{key_hash}

### Description
Retrieve detailed information about a specific API key.

### Method
GET

### Endpoint
`https://openrouter.ai/api/v1/keys/{key_hash}`

### Parameters
#### Path Parameters
- **key_hash** (string) - Required - The unique identifier of the API key to retrieve

#### Headers
- **Authorization** (string) - Required - Bearer token with Management API key format: `Bearer {MANAGEMENT_API_KEY}`
- **Content-Type** (string) - Required - `application/json`

### Request Example
```
GET https://openrouter.ai/api/v1/keys/key_abc123
Headers:
  Authorization: Bearer your-management-key
  Content-Type: application/json
```

### Response
#### Success Response (200)
- **key_hash** (string) - Unique identifier for the key
- **name** (string) - Name of the API key
- **limit** (integer) - Credit limit for the key
- **disabled** (boolean) - Whether the key is disabled
- **limit_reset** (string) - When the limit resets
- **include_byok_in_limit** (boolean) - Whether BYOK usage is included in limit

#### Response Example
```json
{
  "key_hash": "key_abc123",
  "name": "Customer Instance Key",
  "limit": 1000,
  "disabled": false,
  "limit_reset": "daily",
  "include_byok_in_limit": false
}
```
```

--------------------------------

### Create API Key with OpenRouter API - C#

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

C# implementation using the RestSharp library to create an API key. Demonstrates RestClient initialization, request method configuration, header addition, and parameter handling for JSON payloads.

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/keys");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Analytics Service Key\",\n  \"limit\": 150,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true,\n  \"expires_at\": \"2028-06-30T23:59:59Z\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

--------------------------------

### POST /api/v1/chat/completions - Quantization Filter

Source: https://openrouter.ai/docs/guides/routing/provider-selection

Configure the chat completions endpoint to filter providers by quantization level. This example shows how to request FP8 quantization, ensuring the model is only served from providers supporting that specific quantization method.

```APIDOC
## POST /api/v1/chat/completions

### Description
Send a chat completion request to OpenRouter with quantization level filtering to ensure models are served from providers supporting specific quantization methods.

### Method
POST

### Endpoint
https://openrouter.ai/api/v1/chat/completions

### Headers
- **Authorization** (string) - Required - Bearer token with your OpenRouter API key
- **HTTP-Referer** (string) - Required - Your site URL for tracking and rate limiting
- **X-Title** (string) - Required - Your site name for identification
- **Content-Type** (string) - Required - Set to "application/json"

### Request Body
- **model** (string) - Required - Model identifier (e.g., "meta-llama/llama-3.1-8b-instruct")
- **messages** (array) - Required - Array of message objects with role and content
- **provider** (object) - Optional - Provider configuration object
  - **quantizations** (string[]) - Optional - Array of supported quantization levels to filter by
- **stream** (boolean) - Optional - Enable streaming responses (default: false)

### Supported Quantization Levels
- **int4** - Integer (4 bit)
- **int8** - Integer (8 bit)
- **fp4** - Floating point (4 bit)
- **fp6** - Floating point (6 bit)
- **fp8** - Floating point (8 bit)
- **fp16** - Floating point (16 bit)
- **bf16** - Brain floating point (16 bit)
- **fp32** - Floating point (32 bit)
- **unknown** - Unknown quantization

### Request Example
```json
{
  "model": "meta-llama/llama-3.1-8b-instruct",
  "messages": [
    {
      "role": "user",
      "content": "Hello"
    }
  ],
  "provider": {
    "quantizations": ["fp8"]
  },
  "stream": false
}
```

### Response
#### Success Response (200)
- **id** (string) - Unique identifier for the completion
- **object** (string) - Object type ("chat.completion")
- **created** (number) - Unix timestamp of creation
- **model** (string) - Model used for the completion
- **choices** (array) - Array of completion choices
  - **message** (object) - Message object with role and content
  - **finish_reason** (string) - Reason for completion ("stop", "length", etc.)
  - **index** (number) - Index of the choice
- **usage** (object) - Token usage information
  - **prompt_tokens** (number) - Tokens in the prompt
  - **completion_tokens** (number) - Tokens in the completion
  - **total_tokens** (number) - Total tokens used

#### Response Example
```json
{
  "id": "gen-xyz789",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "meta-llama/llama-3.1-8b-instruct",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      "finish_reason": "stop",
      "index": 0
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 12,
    "total_tokens": 22
  }
}
```
```

--------------------------------

### GET /api/v1/keys

Source: https://openrouter.ai/docs/guides/overview/auth/management-api-keys

List all API keys with pagination support. Returns the most recent 100 API keys by default. Use the offset parameter to paginate through additional keys.

```APIDOC
## GET /api/v1/keys

### Description
Retrieve a list of API keys associated with your account. Supports pagination using the offset parameter.

### Method
GET

### Endpoint
`https://openrouter.ai/api/v1/keys`

### Parameters
#### Query Parameters
- **offset** (integer) - Optional - Number of keys to skip for pagination (default: 0)

#### Headers
- **Authorization** (string) - Required - Bearer token with Management API key format: `Bearer {MANAGEMENT_API_KEY}`
- **Content-Type** (string) - Required - `application/json`

### Request Example
```
GET https://openrouter.ai/api/v1/keys?offset=100
Headers:
  Authorization: Bearer your-management-key
  Content-Type: application/json
```

### Response
#### Success Response (200)
- **keys** (array) - List of API key objects
  - **key_hash** (string) - Unique identifier for the key
  - **name** (string) - Name of the API key
  - **limit** (integer) - Credit limit for the key
  - **disabled** (boolean) - Whether the key is disabled
  - **limit_reset** (string) - When the limit resets (e.g., 'daily')

#### Response Example
```json
{
  "keys": [
    {
      "key_hash": "key_abc123",
      "name": "Customer Instance Key",
      "limit": 1000,
      "disabled": false,
      "limit_reset": "daily"
    }
  ]
}
```
```

--------------------------------

### TypeScript SDK Implementation

Source: https://openrouter.ai/docs/guides/features/structured-outputs

Example implementation using the OpenRouter TypeScript SDK to send chat completion requests with structured JSON output format. Demonstrates proper initialization and response handling.

```APIDOC
## TypeScript SDK Implementation

### Description
Implement OpenRouter chat completions with structured outputs using the official TypeScript SDK.

### Code Example
```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '{{API_KEY_REF}}',
});

const response = await openRouter.chat.send({
  model: 'openai/gpt-4',
  messages: [
    { role: 'user', content: 'What is the weather like in London?' },
  ],
  responseFormat: {
    type: 'json_schema',
    jsonSchema: {
      name: 'weather',
      strict: true,
      schema: {
        type: 'object',
        properties: {
          location: {
            type: 'string',
            description: 'City or location name',
          },
          temperature: {
            type: 'number',
            description: 'Temperature in Celsius',
          },
          conditions: {
            type: 'string',
            description: 'Weather conditions description',
          },
        },
        required: ['location', 'temperature', 'conditions'],
        additionalProperties: false,
      },
    },
  },
  stream: false,
});

const weatherInfo = response.choices[0].message.content;
```
```

--------------------------------

### Tiered Pricing Configuration

Source: https://openrouter.ai/docs/use-cases/for-providers

Configure different pricing tiers based on context length. Use this when models have different pricing for long context requests.

```APIDOC
## Tiered Pricing

### Description
For models with different pricing based on context length (e.g., long context pricing), provide `pricing` as an array of tiers instead of a single object.

### Structure
The first tier (index 0) is the base pricing that applies when input tokens are below the `min_context` threshold. The second tier applies when input tokens meet or exceed the `min_context` value.

### Pricing Tier Object
- **prompt** (string) - Pricing per 1 token for prompt
- **completion** (string) - Pricing per 1 token for completion
- **image** (string) - Pricing per 1 image (base tier only)
- **request** (string) - Pricing per 1 request (base tier only)
- **input_cache_read** (string) - Pricing per 1 cached input token
- **min_context** (integer) - Minimum input tokens for this tier to apply (required for non-base tiers)

### Example
```json
{
  "pricing": [
    {
      "prompt": "0.000002",
      "completion": "0.000012",
      "image": "0.01",
      "request": "0",
      "input_cache_read": "0.000001"
    },
    {
      "prompt": "0.000004",
      "completion": "0.000018",
      "input_cache_read": "0.000002",
      "min_context": 200000
    }
  ]
}
```

### Limitations
- Currently, OpenRouter supports up to 2 pricing tiers
- The `image` and `request` fields are only supported in the base tier (index 0) and will be ignored if included in other tiers
```

--------------------------------

### Install Anthropic Agent SDK for TypeScript Projects

Source: https://openrouter.ai/docs/guides/community/anthropic-agent-sdk

Installs the official Anthropic Agent SDK package using npm, which is a prerequisite for developing AI agents in TypeScript. This command adds the SDK to your project's dependencies, allowing you to import and use its functionalities.

```bash
npm install @anthropic-ai/claude-agent-sdk
```

--------------------------------

### Example OpenRouter API Request with Custom Datadog Trace Metadata

Source: https://openrouter.ai/docs/guides/features/broadcast/datadog

This JSON example demonstrates how to include custom metadata within an OpenRouter API request's 'trace' object. This metadata, such as 'trace_name', 'environment', 'team', and 'ticket_id', is then mapped to Datadog spans for enhanced observability, filtering, and analysis in Datadog LLM Observability.

```json
{
  "model": "openai/gpt-4o",
  "messages": [{ "role": "user", "content": "Hello!" }],
  "user": "user_12345",
  "session_id": "session_abc",
  "trace": {
    "trace_name": "Customer Support Bot",
    "environment": "production",
    "team": "support",
    "ticket_id": "TICKET-1234"
  }
}
```

--------------------------------

### Fetch OpenRouter API Keys - C#

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Uses the RestSharp library to create and execute an authenticated GET request to the OpenRouter API. Demonstrates RestSharp client configuration with custom headers.

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

--------------------------------

### Fetch Models Count via HTTP GET Request - Python

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

Python implementation using the requests library to make a GET request to the OpenRouter models count endpoint. Requires a valid Bearer token for authentication and returns the JSON response containing model count data.

```python
import requests

url = "https://openrouter.ai/api/v1/models/count"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

--------------------------------

### List Guardrail Key Assignments using Standalone Function (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/guardrails

This example illustrates how to list API key assignments for a guardrail using a standalone function from the OpenRouter SDK's core module, which is optimized for tree-shaking. It initializes `OpenRouterCore` and then invokes `guardrailsListGuardrailKeyAssignments`, passing the core instance and the guardrail ID. The example also includes basic error handling.

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { guardrailsListGuardrailKeyAssignments } from "@openrouter/sdk/funcs/guardrailsListGuardrailKeyAssignments.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await guardrailsListGuardrailKeyAssignments(openRouter, {
    id: "550e8400-e29b-41d4-a716-446655440000",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("guardrailsListGuardrailKeyAssignments failed:", res.error);
  }
}

run();
```

--------------------------------

### Implement Basic Skills Tool with Context Injection

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

Create a TypeScript implementation of a skills tool that loads specialized skills and injects their context into conversations using nextTurnParams. Includes functions to list available skills, prevent duplicate loading, and execute skill loading with proper error handling.

```typescript
import { OpenRouter, tool } from '@openrouter/sdk';
import { readFileSync, existsSync, readdirSync } from 'fs';
import path from 'path';
import { z } from 'zod';

const openrouter = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

const SKILLS_DIR = path.join(process.env.HOME || '~', '.claude', 'skills');

// List available skills
const listAvailableSkills = (): string[] => {
  if (!existsSync(SKILLS_DIR)) return [];
  return readdirSync(SKILLS_DIR, { withFileTypes: true })
    .filter((dirent) => dirent.isDirectory())
    .filter((dirent) => existsSync(path.join(SKILLS_DIR, dirent.name, 'SKILL.md')))
    .map((dirent) => dirent.name);
};

const skillsTool = tool({
  name: 'Skill',
  description: `Load a specialized skill to enhance the assistant's capabilities.
Available skills: ${listAvailableSkills().join(', ') || 'none configured'}
Each skill provides domain-specific instructions and capabilities.`,

  inputSchema: z.object({
    type: z.string().describe("The skill type to load (e.g., 'pdf-processing')"),
  }),

  outputSchema: z.string(),

  // This is where the magic happens - modify context for next turn
  nextTurnParams: {
    input: (params, context) => {
      // Prevent duplicate skill loading
      const skillMarker = `[Skill: ${params.type}]`;
      if (JSON.stringify(context.input).includes(skillMarker)) {
        return context.input;
      }

      // Load the skill's instructions
      const skillPath = path.join(SKILLS_DIR, params.type, 'SKILL.md');
      if (!existsSync(skillPath)) {
        return context.input;
      }

      const skill = readFileSync(skillPath, 'utf-8');
      const skillDir = path.join(SKILLS_DIR, params.type);

      // Inject skill context into the conversation
      const currentInput = Array.isArray(context.input) ? context.input : [context.input];

      return [
        ...currentInput,
        {
          role: 'user',
          content: `${skillMarker}
Base directory for this skill: ${skillDir}

${skill}`,
        },
      ];
    },
  },

  execute: async (params, context) => {
    const skillMarker = `[Skill: ${params.type}]`;

    // Check if already loaded
    if (JSON.stringify(context?.turnRequest?.input || []).includes(skillMarker)) {
      return `Skill ${params.type} is already loaded`;
    }

    const skillPath = path.join(SKILLS_DIR, params.type, 'SKILL.md');
    if (!existsSync(skillPath)) {
      const available = listAvailableSkills();
      return `Skill "${params.type}" not found. Available skills: ${available.join(', ') || 'none'}`;
    }

    return `Launching skill ${params.type}`;
  },
});
```

--------------------------------

### GET /api/v1/guardrails/{id}

Source: https://openrouter.ai/docs/api/api-reference/guardrails/get-guardrail

Retrieves a specific guardrail configuration by its unique identifier. This endpoint requires bearer token authentication and returns the guardrail settings associated with the provided ID.

```APIDOC
## GET /api/v1/guardrails/{id}

### Description
Retrieves a specific guardrail configuration from OpenRouter using its unique identifier. This endpoint requires authentication via bearer token.

### Method
GET

### Endpoint
https://openrouter.ai/api/v1/guardrails/{id}

### Parameters
#### Path Parameters
- **id** (string) - Required - The unique identifier of the guardrail configuration (UUID format)

#### Headers
- **Authorization** (string) - Required - Bearer token for authentication. Format: "Bearer <token>"

### Request Example
```
GET /api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000 HTTP/1.1
Host: openrouter.ai
Authorization: Bearer <token>
```

### Response
#### Success Response (200)
Returns the guardrail configuration object with all associated settings and metadata.

#### Response Example
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "guardrail_name",
  "settings": {}
}
```

#### Error Response (401)
- **error** (string) - Unauthorized - Invalid or missing authentication token

#### Error Response (404)
- **error** (string) - Not Found - Guardrail configuration with specified ID does not exist
```

--------------------------------

### Use Async Functions for Dynamic Parameters in OpenRouter SDK

Source: https://openrouter.ai/docs/sdks/typescript/call-model/dynamic-parameters

This example shows how to use asynchronous functions for `temperature` and `instructions` parameters. This allows parameters to fetch external data, such as user preferences or business rules from a database, before determining their final value, enhancing the model's adaptive capabilities.

```typescript
const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',

  // Fetch user preferences from database
  temperature: async (ctx) => {
    const prefs = await fetchUserPreferences(userId);
    return prefs.preferredTemperature ?? 0.7;
  },

  // Load dynamic instructions
  instructions: async (ctx) => {
    const rules = await fetchBusinessRules();
    return `Follow these rules:\n${rules.join('\n')}`;
  },

  input: 'Hello!',
});
```

--------------------------------

### Migrate OpenAI SDK Chat Completions to OpenRouter SDK (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/call-model/message-formats

This example illustrates how to refactor code from using the OpenAI SDK for chat completions to the OpenRouter SDK. It provides 'before' and 'after' code, demonstrating the changes in imports, API instantiation, and the `callModel` method with `fromChatMessages` for input conversion.

```typescript
// Before: OpenAI SDK
import OpenAI from 'openai';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const completion = await openai.chat.completions.create({
  model: 'gpt-4',
  messages: [
    { role: 'system', content: 'You are helpful.' },
    { role: 'user', content: 'Hello!' },
  ],
});

// After: OpenRouter SDK
import { OpenRouter, fromChatMessages } from '@openrouter/sdk';

const openrouter = new OpenRouter({ apiKey: process.env.OPENROUTER_API_KEY });
const result = openrouter.callModel({
  model: 'openai/gpt-5.2',
  input: fromChatMessages([
    { role: 'system', content: 'You are helpful.' },
    { role: 'user', content: 'Hello!' },
  ]),
});

const text = await result.getText();
```

--------------------------------

### Understand OpenRouter AI Tool Call Response Format (JSON)

Source: https://openrouter.ai/docs/api/reference/responses/tool-calling

This snippet provides an example of the JSON response structure when the OpenRouter AI API makes a tool call. It highlights the `output` array containing `function_call` objects, detailing the `name` of the tool called and its `arguments`. This format is crucial for processing and executing the suggested tool actions.

```json
{
  "id": "resp_1234567890",
  "object": "response",
  "created_at": 1234567890,
  "model": "openai/o4-mini",
  "output": [
    {
      "type": "function_call",
      "id": "fc_abc123",
      "call_id": "call_xyz789",
      "name": "get_weather",
      "arguments": "{\"location\":\"San Francisco, CA\"}"
    }
  ],
  "usage": {
    "input_tokens": 45,
    "output_tokens": 25,
    "total_tokens": 70
  },
  "status": "completed"
}
```

--------------------------------

### GET /api/v1/keys/{key_hash} - Get API Key

Source: https://openrouter.ai/docs/guides/overview/auth/provisioning-api-keys

Retrieves detailed information about a specific API key using its hash identifier. Returns all key metadata and usage statistics. Requires a Management API key in the Authorization header.

```APIDOC
## GET /api/v1/keys/{key_hash}

### Description
Retrieve detailed information about a specific API key including its configuration and usage statistics.

### Method
GET

### Endpoint
/api/v1/keys/{key_hash}

### Parameters
#### Path Parameters
- **key_hash** (string) - Required - The unique hash identifier of the key to retrieve

#### Headers
- **Authorization** (string) - Required - Management API key in format: Bearer {management_key}

### Request Example
```
GET /api/v1/keys/<YOUR_KEY_HASH>
Authorization: Bearer your-management-key
```

### Response
#### Success Response (200)
- **data** (object) - API key object with all fields including:
  - **created_at** (string) - ISO 8601 timestamp of key creation
  - **updated_at** (string) - ISO 8601 timestamp of last update
  - **hash** (string) - Unique identifier for the key
  - **label** (string) - Masked key label
  - **name** (string) - User-defined name for the key
  - **disabled** (boolean) - Whether the key is disabled
  - **limit** (number) - Credit limit for the key
  - **limit_remaining** (number) - Remaining credits
  - **limit_reset** (string) - Reset frequency
  - **include_byok_in_limit** (boolean) - Whether BYOK usage counts toward limit
  - **usage** (number) - Total usage
  - **usage_daily** (number) - Daily usage
  - **usage_weekly** (number) - Weekly usage
  - **usage_monthly** (number) - Monthly usage
  - **byok_usage** (number) - Total BYOK usage
  - **byok_usage_daily** (number) - Daily BYOK usage
  - **byok_usage_weekly** (number) - Weekly BYOK usage
  - **byok_usage_monthly** (number) - Monthly BYOK usage

#### Response Example
```json
{
  "data": {
    "created_at": "2025-02-19T20:52:27.363244+00:00",
    "updated_at": "2025-02-19T21:24:11.708154+00:00",
    "hash": "<YOUR_KEY_HASH>",
    "label": "sk-or-v1-abc...123",
    "name": "Customer Key",
    "disabled": false,
    "limit": 10,
    "limit_remaining": 10,
    "limit_reset": null,
    "include_byok_in_limit": false,
    "usage": 0,
    "usage_daily": 0,
    "usage_weekly": 0,
    "usage_monthly": 0,
    "byok_usage": 0,
    "byok_usage_daily": 0,
    "byok_usage_weekly": 0,
    "byok_usage_monthly": 0
  }
}
```
```

--------------------------------

### Fetch API Implementation

Source: https://openrouter.ai/docs/guides/features/structured-outputs

Example implementation using native Fetch API in TypeScript to send chat completion requests with structured JSON output format to OpenRouter.

```APIDOC
## Fetch API Implementation

### Description
Implement OpenRouter chat completions with structured outputs using native Fetch API.

### Code Example
```typescript
const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    Authorization: 'Bearer {{API_KEY_REF}}',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'openai/gpt-4',
    messages: [
      { role: 'user', content: 'What is the weather like in London?' },
    ],
    response_format: {
      type: 'json_schema',
      json_schema: {
        name: 'weather',
        strict: true,
        schema: {
          type: 'object',
          properties: {
            location: {
              type: 'string',
              description: 'City or location name',
            },
            temperature: {
              type: 'number',
              description: 'Temperature in Celsius',
            },
            conditions: {
              type: 'string',
              description: 'Weather conditions description',
            },
          },
          required: ['location', 'temperature', 'conditions'],
          additionalProperties: false,
        },
      },
    },
  }),
});

const data = await response.json();
const weatherInfo = data.choices[0].message.content;
```
```

--------------------------------

### List Model Endpoints using OpenRouter SDK (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/endpoints

This example demonstrates how to fetch all available endpoints for a specific model using the `openRouter.endpoints.list` method in the OpenRouter TypeScript SDK. It initializes the SDK with an API key and logs the returned endpoint data.

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.endpoints.list({
    author: "<value>",
    slug: "<value>",
  });

  console.log(result);
}

run();
```

--------------------------------

### Retrieve API Key Information - Java

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key

Executes an authenticated GET request using the Unirest HTTP client library. Adds Bearer token to request headers and returns response as string.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/key")
  .header("Authorization", "Bearer <token>")
  .asString();
```

--------------------------------

### Budget-Based Thinking Configuration

Source: https://openrouter.ai/docs/guides/guides/model-migrations/claude-4-6

Configure Claude 4.6 with budget-based thinking by explicitly setting max_tokens, maintaining backward compatibility with previous reasoning implementations.

```APIDOC
## Budget-Based Thinking

### Description
Enable budget-based thinking for Claude 4.6 by explicitly setting a maximum token budget for the reasoning process.

### Request Parameters
- **model** (string) - Required - Use `anthropic/claude-4.6-opus` or `anthropic/claude-4.6-sonnet`
- **reasoning.enabled** (boolean) - Required - Set to `true` to enable reasoning
- **reasoning.max_tokens** (integer) - Required - Maximum tokens for reasoning (e.g., 10000)

### Request Example
```json
{
  "model": "anthropic/claude-4.6-opus",
  "reasoning": {
    "enabled": true,
    "max_tokens": 10000
  }
}
```

### Behavior
- When `reasoning.max_tokens` is explicitly set, budget-based thinking is used instead of adaptive
- This maintains backward compatibility with previous Claude versions
- Still supported for Claude 4.6 models
```

--------------------------------

### Fetch Models List - PHP with Guzzle

Source: https://openrouter.ai/docs/api/api-reference/models/get-models

Uses Guzzle HTTP client library for PHP to make GET request to OpenRouter API. Requires Composer autoloader and Guzzle package. Returns response body containing models data.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Python Implementation

Source: https://openrouter.ai/docs/guides/features/structured-outputs

Example implementation using Python's requests library to send chat completion requests with structured JSON output format to OpenRouter API.

```APIDOC
## Python Implementation

### Description
Implement OpenRouter chat completions with structured outputs using Python requests library.

### Code Example
```python
import requests
import json

response = requests.post(
  "https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {{API_KEY_REF}}",
    "Content-Type": "application/json",
  },
  json={
    "model": "openai/gpt-4",
    "messages": [
      {"role": "user", "content": "What is the weather like in London?"},
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "weather",
        "strict": True,
        "schema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "City or location name",
            },
            "temperature": {
              "type": "number",
              "description": "Temperature in Celsius",
            },
            "conditions": {
              "type": "string",
              "description": "Weather conditions description",
            },
          },
          "required": ["location", "temperature", "conditions"],
          "additionalProperties": False,
        },
      },
    },
  },
)

data = response.json()
weather_info = data["choices"][0]["message"]["content"]
```
```

--------------------------------

### Send Chat Request with Reasoning Tokens using OpenRouter TypeScript SDK

Source: https://openrouter.ai/docs/best-practices/reasoning-tokens

This TypeScript example demonstrates how to initialize the OpenRouter SDK and send a chat completion request, explicitly setting a 'high' reasoning effort. It then logs both the extracted reasoning tokens and the final content from the model's response, showcasing how to access these fields.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '{{API_KEY_REF}}',
});

const response = await openRouter.chat.send({
  model: '{{MODEL}}',
  messages: [
    {
      role: 'user',
      content: "How would you build the world's tallest skyscraper?",
    },
  ],
  reasoning: {
    effort: 'high',
  },
  stream: false,
});

console.log('REASONING:', response.choices[0].message.reasoning);
console.log('CONTENT:', response.choices[0].message.content);
```

--------------------------------

### Import and Initialize ChatGenerationParamsProvider - TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/chatgenerationparamsprovider

Demonstrates how to import the ChatGenerationParamsProvider class from the OpenRouter SDK and initialize an instance with an empty configuration object. This is the basic setup required to use the ChatGenerationParamsProvider in your TypeScript application.

```typescript
import { ChatGenerationParamsProvider } from "@openrouter/sdk/models";

let value: ChatGenerationParamsProvider = {};
```

--------------------------------

### POST /api/v1/chat/completions (Floor Price Shortcut)

Source: https://openrouter.ai/docs/guides/routing/provider-selection

Sends a chat completion request, prioritizing models by price using the `:floor` shortcut appended to the model slug. This is equivalent to setting `provider.sort` to `"price"`.

```APIDOC
## POST /api/v1/chat/completions

### Description
Sends a chat completion request, prioritizing models by price using the `:floor` shortcut appended to the model slug. This is equivalent to setting `provider.sort` to `"price"`.

### Method
POST

### Endpoint
/api/v1/chat/completions

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
- **model** (string) - Required - The model slug, with `:floor` appended to prioritize by price (e.g., `"meta-llama/llama-3.3-70b-instruct:floor"`).
- **messages** (array of objects) - Required - A list of message objects in the conversation.
- **stream** (boolean) - Optional - Whether to stream the response. Defaults to `false`.

### Request Example
```json
{
  "model": "meta-llama/llama-3.3-70b-instruct:floor",
  "messages": [
    {
      "role": "user",
      "content": "Hello"
    }
  ],
  "stream": false
}
```

### Response
#### Success Response (200)
- **id** (string) - Unique identifier for the completion.
- **choices** (array) - List of completion choices.
- **created** (integer) - Timestamp of creation.
- **model** (string) - The model used for the completion.
- **object** (string) - Type of object (e.g., "chat.completion").
- **usage** (object) - Token usage statistics.

#### Response Example
```json
{
  "id": "chatcmpl-xxxxxxxxxxxxxxxxxxxxx",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! How can I assist you today?",
        "role": "assistant"
      }
    }
  ],
  "created": 1677652288,
  "model": "meta-llama/llama-3.3-70b-instruct:floor",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 10,
    "prompt_tokens": 5,
    "total_tokens": 15
  }
}
```
```

--------------------------------

### Preserving Reasoning Blocks for Tool Calling with OpenRouter and Python

Source: https://openrouter.ai/docs/best-practices/reasoning-tokens

This Python example demonstrates how to use the OpenRouter API to preserve reasoning blocks during tool calling. It shows an initial API call with a tool definition and `reasoning_details` in `extra_body`, followed by a second call where the `reasoning_details` from the assistant's response are passed back to maintain context and allow the model to continue its reasoning after receiving tool results.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="{{API_KEY_REF}}",
)

# Define tools once and reuse
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            },
            "required": ["location"]
        }
    }
}]

# First API call with tools
# Note: You can use 'openai/gpt-5.2' instead of 'anthropic/claude-sonnet-4.5' - they're completely interchangeable
response = client.chat.completions.create(
    model="{{MODEL}}",
    messages=[
        {"role": "user", "content": "What's the weather like in Boston? Then recommend what to wear."}
    ],
    tools=tools,
    extra_body={"reasoning": {"max_tokens": 2000}}
)

# Extract the assistant message with reasoning_details
message = response.choices[0].message

# Preserve the complete reasoning_details when passing back
messages = [
    {"role": "user", "content": "What's the weather like in Boston? Then recommend what to wear."},
    {
        "role": "assistant",
        "content": message.content,
        "tool_calls": message.tool_calls,
        "reasoning_details": message.reasoning_details  # Pass back unmodified
    },
    {
        "role": "tool",
        "tool_call_id": message.tool_calls[0].id,
        "content": '{"temperature": 45, "condition": "rainy", "humidity": 85}'
    }
]

# Second API call - Claude continues reasoning from where it left off
response2 = client.chat.completions.create(
    model="{{MODEL}}",
    messages=messages,  # Includes preserved thinking blocks
    tools=tools
)
```

--------------------------------

### GET /models

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/models

List all models and their properties, providing comprehensive details about each available model.

```APIDOC
## GET /models

### Description
List all models and their properties

### Method
GET

### Endpoint
/models

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
{}

### Request Example
{}

### Response
#### Success Response (200)
- **data** (array) - A list of model objects, each with its properties.
  - **id** (string) - The unique identifier for the model.
  - **name** (string) - The human-readable name of the model.
  - **provider** (object) - Information about the model's provider.
    - **id** (string) - The provider's unique identifier.
    - **name** (string) - The provider's human-readable name.
  - **pricing** (object) - Pricing details for the model.
    - **prompt** (string) - Cost per 1k prompt tokens.
    - **completion** (string) - Cost per 1k completion tokens.
    - **unit** (string) - Unit of pricing (e.g., "1k tokens").

#### Response Example
[
  {
    "id": "openai/gpt-3.5-turbo",
    "name": "GPT-3.5 Turbo",
    "provider": {
      "id": "openai",
      "name": "OpenAI"
    },
    "pricing": {
      "prompt": "0.0015",
      "completion": "0.002",
      "unit": "1k tokens"
    }
  },
  {
    "id": "google/gemini-pro",
    "name": "Gemini Pro",
    "provider": {
      "id": "google",
      "name": "Google"
    },
    "pricing": {
      "prompt": "0.00025",
      "completion": "0.0005",
      "unit": "1k tokens"
    }
  }
]

#### Error Response (500)
- **error** (string) - A description of the internal server error.

#### Error Response (4XX, 5XX)
- **error** (string) - A general error message.

#### Error Example
{
  "error": "Internal Server Error"
}
```

--------------------------------

### Install Anthropic Agent SDK for Python Projects

Source: https://openrouter.ai/docs/guides/community/anthropic-agent-sdk

Installs the official Anthropic Agent SDK package using pip, which is essential for developing AI agents in Python. This command adds the SDK to your Python environment, enabling access to its functions and classes for agent development.

```bash
pip install claude-agent-sdk
```

--------------------------------

### Bulk Assign Members to Guardrail using Standalone Function (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/guardrails

This example illustrates how to use the standalone `guardrailsBulkAssignMembers` function from the OpenRouter SDK for improved tree-shaking performance. It initializes `OpenRouterCore` with an API key and then invokes the standalone function, passing the core instance and the guardrail assignment details. The example also demonstrates how to handle both successful responses and errors.

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { guardrailsBulkAssignMembers } from "@openrouter/sdk/funcs/guardrailsBulkAssignMembers.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await guardrailsBulkAssignMembers(openRouter, {
    id: "550e8400-e29b-41d4-a716-446655440000",
    requestBody: {
      memberUserIds: [
        "user_abc123",
        "user_def456",
      ],
    },
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("guardrailsBulkAssignMembers failed:", res.error);
  }
}

run();
```

--------------------------------

### Retrieve API Key Information - Ruby

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key

Uses Ruby's Net::HTTP library to make an HTTPS GET request with Bearer token authentication. Establishes SSL connection and outputs response body.

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/key")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

--------------------------------

### Implement OpenRouter API Streaming Responses in TypeScript and Python

Source: https://openrouter.ai/docs/api/reference/responses/basic-usage

These code examples demonstrate how to make a streaming request to the OpenRouter API and process the Server-Sent Events (SSE) chunks. They show how to set up the request with 'stream: true' and parse the incoming 'data:' lines, handling '[DONE]' signals and JSON parsing for incremental content delivery.

```typescript
const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: 'Write a short story about AI',
      stream: true,
      max_output_tokens: 9000,
    }),
  });

  const reader = response.body?.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    const lines = chunk.split('\n');

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const data = line.slice(6);
        if (data === '[DONE]') return;

        try {
          const parsed = JSON.parse(data);
          console.log(parsed);
        } catch (e) {
          // Skip invalid JSON
        }
      }
    }
  }
```

```python
import requests
import json

response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': 'Write a short story about AI',
          'stream': True,
          'max_output_tokens': 9000,
      },
      stream=True
  )

  for line in response.iter_lines():
      if line:
          line_str = line.decode('utf-8')
          if line_str.startswith('data: '):
              data = line_str[6:]
              if data == '[DONE]':
                  break
              try:
                  parsed = json.loads(data)
                  print(parsed)
              except json.JSONDecodeError:
                  continue
```

--------------------------------

### Create API Key with OpenRouter API - Java

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

Java implementation using the Unirest HTTP client library to create an API key. Demonstrates fluent API pattern for building HTTP requests with headers and JSON body payload.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/keys")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Analytics Service Key\",\n  \"limit\": 150,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true,\n  \"expires_at\": \"2028-06-30T23:59:59Z\"\n}")
  .asString();
```

--------------------------------

### Best Practice: Using Sensible Defaults for Dynamic Parameters (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/call-model/dynamic-parameters

This example emphasizes the importance of providing sensible default or fallback values for dynamic parameters. If a preferred model cannot be determined, a default like 'openai/gpt-5-nano' ensures the application remains robust and functional.

```typescript
model: (ctx) => {
  const preferredModel = getPreferredModel();
  return preferredModel ?? 'openai/gpt-5-nano'; // Default fallback
},
```

--------------------------------

### Retrieve Current API Key Metadata (Python)

Source: https://openrouter.ai/docs/sdks/python/api-reference/apikeys

This Python example shows how to fetch metadata for the API key currently used for authentication. It initializes the OpenRouter client and then invokes the `api_keys.get_current_key_metadata` method. The response object `res` will contain details about the active API key.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.api_keys.get_current_key_metadata()

    # Handle response
    print(res)
```

--------------------------------

### Create API Key with OpenRouter API - PHP

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

PHP implementation using the Guzzle HTTP client library to create an API key. Demonstrates dependency injection pattern with autoloader and fluent request configuration for POST requests.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/keys', [
  'body' => '{
  "name": "Analytics Service Key",
  "limit": 150,
  "limit_reset": "monthly",
  "include_byok_in_limit": true,
  "expires_at": "2028-06-30T23:59:59Z"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Import and Initialize PublicEndpoint TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/publicendpoint

Demonstrates how to import the PublicEndpoint type from the OpenRouter SDK and create an instance with model information, pricing details, and performance metrics. This example shows a complete PublicEndpoint object for the OpenAI GPT-4 model with all available properties including context length, supported parameters, and latency/throughput statistics.

```typescript
import { PublicEndpoint } from "@openrouter/sdk/models";

let value: PublicEndpoint = {
  name: "OpenAI: GPT-4",
  modelId: "openai/gpt-4",
  modelName: "GPT-4",
  contextLength: 8192,
  pricing: {
    prompt: "0.00003",
    completion: "0.00006"
  },
  providerName: "OpenAI",
  tag: "openai",
  quantization: "fp16",
  maxCompletionTokens: 4096,
  maxPromptTokens: 8192,
  supportedParameters: [
    "temperature",
    "top_p",
    "max_tokens"
  ],
  uptimeLast30m: 99.5,
  supportsImplicitCaching: true,
  latencyLast30m: {
    p50: 0.25,
    p75: 0.35,
    p90: 0.48,
    p99: 0.85
  },
  throughputLast30m: {
    p50: 45.2,
    p75: 38.5,
    p90: 28.3,
    p99: 15.1
  }
};
```

--------------------------------

### Stream Chat Completion with Anthropic Reasoning Tokens

Source: https://openrouter.ai/docs/best-practices/reasoning-tokens

Demonstrates streaming chat completions using Anthropic Claude models with reasoning tokens enabled via the OpenRouter API. The example shows how to configure max_tokens for reasoning, handle streaming responses, and extract reasoning details from chunks. Requires OpenAI Python client configured with OpenRouter base URL and API key.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="{{API_KEY_REF}}",
)

def chat_completion_with_reasoning(messages):
    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=messages,
        max_tokens=10000,
        extra_body={
            "reasoning": {
                "max_tokens": 8000
            }
        },
        stream=True
    )
    return response

for chunk in chat_completion_with_reasoning([
    {"role": "user", "content": "What's bigger, 9.9 or 9.11?"}
]):
    if hasattr(chunk.choices[0].delta, 'reasoning_details') and chunk.choices[0].delta.reasoning_details:
        print(f"REASONING_DETAILS: {chunk.choices[0].delta.reasoning_details}")
    elif getattr(chunk.choices[0].delta, 'content', None):
        print(f"CONTENT: {chunk.choices[0].delta.content}")
```

--------------------------------

### Configure Tool Choice Parameter in JSON

Source: https://openrouter.ai/docs/guides/features/tool-calling

These JSON examples illustrate how to control the model's tool usage behavior using the `tool_choice` parameter. Options include letting the model decide (`auto`), disabling tool usage entirely (`none`), or forcing the use of a specific function by name.

```json
{ "tool_choice": "auto" }
```

```json
{ "tool_choice": "none" }
```

```json
{
  "tool_choice": {
    "type": "function",
    "function": {"name": "search_database"}
  }
}
```

--------------------------------

### GET /key - Get Current Key Metadata

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/apikeys

Retrieves information on the API key associated with the current authentication session. This endpoint requires valid authentication credentials and returns key metadata or error responses for unauthorized, not found, rate limit, or server errors.

```APIDOC
## GET /key

### Description
Get information on the API key associated with the current authentication session

### Method
GET

### Endpoint
/key

### Parameters
#### Request Options
- **request** (operations.GetKeyRequest) - Required - The request object to use for the request
- **options** (RequestOptions) - Optional - Used to set various options for making HTTP requests
- **options.fetchOptions** (RequestInit) - Optional - Options that are passed to the underlying HTTP request. This can be used to inject extra headers. All Request options, except method and body, are allowed
- **options.retries** (RetryConfig) - Optional - Enables retrying HTTP requests under certain failure conditions

### Response
**Promise<operations.GetKeyResponse>**

#### Success Response (200)
Returns key metadata associated with the current authentication session

### Error Handling
| Error Type | Status Code | Content Type |
|---|---|---|
| UnauthorizedResponseError | 401 | application/json |
| NotFoundResponseError | 404 | application/json |
| TooManyRequestsResponseError | 429 | application/json |
| InternalServerResponseError | 500 | application/json |
| OpenRouterDefaultError | 4XX, 5XX | */* |

### Request Example (TypeScript)
```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.apiKeys.getCurrentKeyMetadata();
  console.log(result);
}

run();
```

### Standalone Function Example (TypeScript)
```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { apiKeysGetCurrentKeyMetadata } from "@openrouter/sdk/funcs/apiKeysGetCurrentKeyMetadata.js";

const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await apiKeysGetCurrentKeyMetadata(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("apiKeysGetCurrentKeyMetadata failed:", res.error);
  }
}

run();
```
```

--------------------------------

### POST /chat/completions - Step 1: Initial Inference with Tools

Source: https://openrouter.ai/docs/guides/features/tool-calling

Initiate a chat completion request, providing the LLM with a list of available tools. The model will analyze the user's prompt and suggest tool calls if they are relevant to fulfill the request.

```APIDOC
## POST /chat/completions

### Description
Initiate a chat completion request, providing the LLM with a list of available tools. The model will analyze the user's prompt and suggest tool calls if they are relevant to fulfill the request.

### Method
POST

### Endpoint
/chat/completions

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
- **model** (string) - Required - The ID of the model to use (e.g., "google/gemini-3-flash-preview").
- **messages** (array of objects) - Required - A list of messages comprising the conversation so far.
  - **role** (string) - Required - The role of the author of this message (e.g., "user").
  - **content** (string) - Required - The contents of the message.
- **tools** (array of objects) - Optional - A list of tools the model may call.
  - **type** (string) - Required - The type of the tool (e.g., "function").
  - **function** (object) - Required - The function definition.
    - **name** (string) - Required - The name of the function to be called.
    - **description** (string) - Optional - A description of what the function does.
    - **parameters** (object) - Required - The parameters the function accepts, described as a JSON Schema object.
      - **type** (string) - Required - Always "object".
      - **properties** (object) - Required - The properties of the function's parameters.
        - **search_terms** (array of strings) - Required - List of search terms to find books.
      - **required** (array of strings) - Required - A list of parameter names that are required (e.g., ["search_terms"]).

### Request Example
```json
{
  "model": "google/gemini-3-flash-preview",
  "messages": [
    {
      "role": "user",
      "content": "What are the titles of some James Joyce books?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "search_gutenberg_books",
        "description": "Search for books in the Project Gutenberg library",
        "parameters": {
          "type": "object",
          "properties": {
            "search_terms": {
              "type": "array",
              "items": {"type": "string"},
              "description": "List of search terms to find books"
            }
          },
          "required": ["search_terms"]
        }
      }
    }
  ]
}
```

### Response
#### Success Response (200)
- **id** (string) - The ID of the chat completion.
- **choices** (array of objects) - A list of chat completion choices.
  - **message** (object) - The message generated by the model.
    - **role** (string) - The role of the author of this message, typically "assistant".
    - **content** (string) - The contents of the message, which may be null if tool_calls are present.
    - **tool_calls** (array of objects) - A list of tool calls suggested by the model.
      - **id** (string) - The ID of the tool call.
      - **type** (string) - The type of the tool call (e.g., "function").
      - **function** (object) - The function details.
        - **name** (string) - The name of the function to call.
        - **arguments** (string) - The arguments to call the function with, as a JSON string.

#### Response Example
```json
{
  "id": "chatcmpl-123",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": null,
        "tool_calls": [
          {
            "id": "call_abc123",
            "type": "function",
            "function": {
              "name": "search_gutenberg_books",
              "arguments": "{\"search_terms\": [\"James\", \"Joyce\"]}"
            }
          }
        ]
      }
    }
  ]
}
```
```

--------------------------------

### Generate Text with Multimodal Input including Images (TypeScript)

Source: https://openrouter.ai/docs/sdks/call-model/text-generation

This example demonstrates how to send multimodal input to `callModel`, combining text and an image URL within a message object for models that support rich content.

```typescript
const result = openrouter.callModel({
  model: 'openai/gpt-5.2',
  input: [
    {
      type: 'message',
      role: 'user',
      content: [
        { type: 'input_text', text: 'What is in this image?' },
        {
          type: 'input_image',
          imageUrl: 'https://example.com/image.jpg',
          detail: 'auto',
        },
      ],
    },
  ],
});
```

--------------------------------

### GET OpenRouter Guardrails API - C#

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

Uses RestSharp library to make a GET request to the OpenRouter guardrails API. Creates a RestClient instance, adds the Authorization header with Bearer token, and executes the request.

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/guardrails");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

--------------------------------

### Model Configuration - Quantization Options

Source: https://openrouter.ai/docs/api/api-reference/embeddings/create-embeddings

Enumeration of supported quantization formats for model optimization. Includes various precision levels from int4 to fp32 for different performance and accuracy trade-offs.

```APIDOC
## Quantization Schema

### Description
Supported quantization formats for model optimization and deployment.

### Supported Quantization Types
- **int4** - 4-bit integer quantization
- **int8** - 8-bit integer quantization
- **fp4** - 4-bit floating point quantization
- **fp6** - 6-bit floating point quantization
- **fp8** - 8-bit floating point quantization
- **fp16** - 16-bit floating point (half precision)
- **bf16** - Brain float 16-bit format
- **fp32** - 32-bit floating point (full precision)
- **unknown** - Quantization type not specified or unknown

### Usage
Specify quantization type when configuring model deployment or inference parameters to optimize for latency, memory usage, or accuracy requirements.
```

--------------------------------

### Create a response using standalone `betaResponsesSend` function

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/responses

This example illustrates the usage of the `betaResponsesSend` standalone function, which is recommended for optimal tree-shaking performance. It initializes `OpenRouterCore`, calls the function with the core instance, and includes error handling for the response.

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { betaResponsesSend } from "@openrouter/sdk/funcs/betaResponsesSend.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await betaResponsesSend(openRouter, {});
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("betaResponsesSend failed:", res.error);
  }
}

run();
```

--------------------------------

### Instantiate GetKeyRequest Object in TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getkeyrequest

This TypeScript example demonstrates how to create an instance of the `GetKeyRequest` object from the `@openrouter/sdk/models/operations` module. It shows the structure for providing the required `hash` property to identify an API key.

```typescript
import { GetKeyRequest } from "@openrouter/sdk/models/operations";

let value: GetKeyRequest = {
  hash: "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943"
};
```

--------------------------------

### GET OpenRouter Guardrails API - Java

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

Executes a GET request to the OpenRouter guardrails API using the Unirest HTTP client library. Adds Authorization header with Bearer token and returns the response as a string.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/guardrails")
  .header("Authorization", "Bearer <token>")
  .asString();
```

--------------------------------

### Create OAuth Authorization Code in OpenRouter Python SDK

Source: https://openrouter.ai/docs/sdks/python/api-reference/oauth

This Python example illustrates how to create an authorization code for the PKCE flow to generate a user-controlled API key. It initializes the OpenRouter client and invokes the `o_auth.create_auth_code` method, providing a callback URL. The method returns the newly generated authorization code.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.o_auth.create_auth_code(callback_url="https://myapp.com/auth/callback")

    # Handle response
    print(res)
```

--------------------------------

### GET /key

Source: https://openrouter.ai/docs/sdks/python/api-reference/apikeys

Fetches metadata for the API key currently used for authentication in the active session.

```APIDOC
## GET /key

### Description
Fetches metadata for the API key currently used for authentication in the active session.

### Method
GET

### Endpoint
/key

### Parameters
#### Path Parameters
(None)

### Response
#### Success Response (200)
- **Response Type** (operations.GetCurrentKeyResponse) - Contains metadata about the current API key.
```

--------------------------------

### Fetch Models List - Java with Unirest

Source: https://openrouter.ai/docs/api/api-reference/models/get-models

Leverages the Unirest HTTP library for Java to perform GET request with Bearer token authentication. Returns HttpResponse object containing the models data as a string.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models")
  .header("Authorization", "Bearer <token>")
  .asString();
```

--------------------------------

### Maximize BYOK Usage with `partition: "none"` in OpenRouter Chat API

Source: https://openrouter.ai/docs/guides/routing/provider-selection

This code demonstrates how to configure OpenRouter API requests to maximize Bring Your Own Key (BYOK) usage across multiple models. By setting `provider.sort.partition` to `"none"`, OpenRouter can route to a fallback model that supports BYOK if the primary model does not, ensuring your own API keys are utilized effectively. This example sends a chat completion request with a list of models and the specified provider sorting.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
});

const completion = await openRouter.chat.send({
  models: [
    'anthropic/claude-sonnet-4.5',
    'openai/gpt-5-mini',
    'google/gemini-3-flash-preview',
  ],
  messages: [{ role: 'user', content: 'Hello' }],
  provider: {
    sort: {
      by: 'price',
      partition: 'none',
    },
  },
  stream: false,
});
```

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer <OPENROUTER_API_KEY>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    models: [
      'anthropic/claude-sonnet-4.5',
      'openai/gpt-5-mini',
      'google/gemini-3-flash-preview',
    ],
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      sort: {
        by: 'price',
        partition: 'none',
      },
    },
  }),
});
```

```python
import requests

headers = {
  'Authorization': 'Bearer <OPENROUTER_API_KEY>',
  'Content-Type': 'application/json',
}

response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
  'models': [
    'anthropic/claude-sonnet-4.5',
    'openai/gpt-5-mini',
    'google/gemini-3-flash-preview',
  ],
  'messages': [{ 'role': 'user', 'content': 'Hello' }],
  'provider': {
    'sort': {
      'by': 'price',
      'partition': 'none',
    },
  },
})
```

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer <OPENROUTER_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "models": [
      "anthropic/claude-sonnet-4.5",
      "openai/gpt-5-mini",
      "google/gemini-3-flash-preview"
    ],
    "messages": [{ "role": "user", "content": "Hello" }],
    "provider": {
      "sort": {
        "by": "price",
        "partition": "none"
      }
    }
  }'
```

--------------------------------

### Bulk Assign API Keys to Guardrail (Python)

Source: https://openrouter.ai/docs/sdks/python/api-reference/guardrails

This Python example illustrates how to assign multiple API keys to a specific guardrail in bulk using the OpenRouter SDK. It initializes the client with an API key obtained from environment variables and then invokes the `bulk_assign_keys` method. The method requires the guardrail's unique identifier and a list of API key hashes to be assigned. The response from the operation is then printed.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.bulk_assign_keys(id="550e8400-e29b-41d4-a716-446655440000", key_hashes=[
        "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93",
    ])

    # Handle response
    print(res)
```

--------------------------------

### Fetch Models Count via HTTP GET Request - JavaScript

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

JavaScript implementation using the Fetch API to retrieve the models count from OpenRouter. Includes error handling and async/await syntax for managing the asynchronous HTTP request.

```javascript
const url = 'https://openrouter.ai/api/v1/models/count';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

--------------------------------

### Fetch Models List - C# with RestSharp

Source: https://openrouter.ai/docs/api/api-reference/models/get-models

Implements HTTP GET request using RestSharp library for C#. Creates RestClient and RestRequest objects with Authorization header. Executes request and returns IRestResponse object.

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/models");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

--------------------------------

### Start OpenClaw gateway service (Bash)

Source: https://openrouter.ai/docs/guides/guides/openclaw-integration

This command initiates or restarts the OpenClaw gateway service. After configuring API keys and models, running this command ensures that OpenClaw agents begin using OpenRouter to route requests to the chosen LLM.

```bash
openclaw gateway run
```

--------------------------------

### GET OpenRouter Guardrails API - Go

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

Constructs and executes an HTTP GET request to the OpenRouter guardrails API using Go's net/http package. Sets Authorization header with Bearer token and reads the response body. Handles resource cleanup with defer.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/guardrails"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### GET /endpoints/zdr

Source: https://openrouter.ai/docs/sdks/python/api-reference/endpoints

Preview the impact of ZDR on the available endpoints.

```APIDOC
## GET /endpoints/zdr

### Description
Preview the impact of ZDR on the available endpoints

### Method
GET

### Endpoint
/endpoints/zdr

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(None)

### Response
#### Success Response (200)
- **Response Type**: operations.ListEndpointsZdrResponse

#### Response Example
(None)

#### Error Responses
- **500 Internal Server Error**: errors.InternalServerResponseError
- **4XX, 5XX Generic Error**: errors.OpenRouterDefaultError
```

--------------------------------

### Migrate Anthropic SDK Messages to OpenRouter SDK (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/call-model/message-formats

This example demonstrates how to convert code from using the Anthropic SDK for message creation to the OpenRouter SDK. It provides 'before' and 'after' code, highlighting the changes in imports, API instantiation, and the `callModel` method with `fromClaudeMessages` for input conversion and `maxOutputTokens`.

```typescript
// Before: Anthropic SDK
import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic();
const message = await anthropic.messages.create({
  model: 'claude-sonnet-4-20250514',
  max_tokens: 1024,
  messages: [
    { role: 'user', content: 'Hello!' },
  ],
});

// After: OpenRouter SDK
import { OpenRouter, fromClaudeMessages } from '@openrouter/sdk';

const openrouter = new OpenRouter({ apiKey: process.env.OPENROUTER_API_KEY });
const result = openrouter.callModel({
  model: 'anthropic/claude-sonnet-4.5',
  input: fromClaudeMessages([
    { role: 'user', content: 'Hello!' },
  ]),
  maxOutputTokens: 1024,
});

const text = await result.getText();
```

--------------------------------

### Create API Key with OpenRouter API - JavaScript

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

JavaScript implementation using the Fetch API to create an API key with rate limiting configuration. Includes error handling with try-catch block and async/await pattern for handling the asynchronous HTTP request.

```javascript
const url = 'https://openrouter.ai/api/v1/keys';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"name":"Analytics Service Key","limit":150,"limit_reset":"monthly","include_byok_in_limit":true,"expires_at":"2028-06-30T23:59:59Z"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

--------------------------------

### GET /api/v1/activity

Source: https://openrouter.ai/docs/api/api-reference/analytics/get-user-activity

This endpoint returns user activity data grouped by endpoint for the last 30 (completed) UTC days. A management API key is required for authentication.

```APIDOC
## GET /api/v1/activity

### Description
Returns user activity data grouped by endpoint for the last 30 (completed) UTC days. A management key is required.

### Method
GET

### Endpoint
https://openrouter.ai/api/v1/activity

### Parameters
#### Header Parameters
- **Authorization** (string) - Required - API key as bearer token in Authorization header

#### Query Parameters
- **date** (string) - Optional - Filter by a single UTC date in the last 30 days (YYYY-MM-DD format).

#### Request Body
(None)

### Request Example
{}

### Response
#### Success Response (200)
- **data** (array of ActivityItem) - List of activity items
  - **ActivityItem** (object)
    - **date** (string) - Required - Date of the activity (YYYY-MM-DD format)
    - **model** (string) - Required - Model slug (e.g., "openai/gpt-4.1")
    - **model_permaslug** (string) - Required - Model permaslug (e.g., "openai/gpt-4.1-2025-04-14")
    - **endpoint_id** (string) - Required - Unique identifier for the endpoint
    - **provider_name** (string) - Required - Name of the provider serving this endpoint
    - **usage** (number) - Required - Total cost in USD (OpenRouter credits spent)
    - **byok_usage_inference** (number) - Required - BYOK inference cost in USD (external credits spent)
    - **requests** (number) - Required - Number of requests made
    - **prompt_tokens** (number) - Required - Total prompt tokens used
    - **completion_tokens** (number) - Required - Total completion tokens generated
    - **reasoning_tokens** (number) - Required - Total reasoning tokens used

#### Response Example
```json
{
  "data": [
    {
      "date": "2024-01-01",
      "model": "openai/gpt-4.1",
      "model_permaslug": "openai/gpt-4.1-2025-04-14",
      "endpoint_id": "some_endpoint_id_123",
      "provider_name": "OpenAI",
      "usage": 0.05,
      "byok_usage_inference": 0.0,
      "requests": 10,
      "prompt_tokens": 1000,
      "completion_tokens": 500,
      "reasoning_tokens": 0
    },
    {
      "date": "2024-01-02",
      "model": "google/gemini-pro",
      "model_permaslug": "google/gemini-pro-2024-03-15",
      "endpoint_id": "another_endpoint_id_456",
      "provider_name": "Google",
      "usage": 0.02,
      "byok_usage_inference": 0.01,
      "requests": 5,
      "prompt_tokens": 300,
      "completion_tokens": 150,
      "reasoning_tokens": 0
    }
  ]
}
```
```

--------------------------------

### Best Practice: Design Idempotent OpenRouter AI Tools (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/call-model/tools

This snippet illustrates how to design idempotent tools, meaning they can be safely called multiple times without producing different results beyond the initial execution. The example shows checking for an existing user before creation, ensuring that calling the tool repeatedly does not create duplicate entries.

```typescript
const createUserTool = tool({
  name: 'create_user',
  inputSchema: z.object({
    email: z.string().email(),
    name: z.string(),
  }),
  execute: async (params) => {
    // Check if user exists first
    const existing = await findUserByEmail(params.email);
    if (existing) {
      return { userId: existing.id, created: false };
    }

    const user = await createUser(params);
    return { userId: user.id, created: true };
  },
});
```

--------------------------------

### GET OpenRouter Guardrails API - Python

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

Makes a GET request to the OpenRouter guardrails API endpoint using the requests library. Requires a valid Bearer token for authentication. Returns parsed JSON response from the API.

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

--------------------------------

### GET /keys/{hash}

Source: https://openrouter.ai/docs/sdks/python/api-reference/apikeys

Retrieves details for a single API key identified by its hash. This operation requires a provisioning key.

```APIDOC
## GET /keys/{hash}

### Description
Retrieves details for a single API key identified by its hash. This operation requires a provisioning key.

### Method
GET

### Endpoint
/keys/{hash}

### Parameters
#### Path Parameters
- **hash** (str) - Required - The hash identifier of the API key to retrieve

### Response
#### Success Response (200)
- **Response Type** (operations.GetKeyResponse) - Contains the details of the requested API key.

### Error Handling
- **errors.UnauthorizedResponseError** (401) - application/json
- **errors.NotFoundResponseError** (404) - application/json
- **errors.TooManyRequestsResponseError** (429) - application/json
- **errors.InternalServerResponseError** (500) - application/json
- **errors.OpenRouterDefaultError** (4XX, 5XX) - */*
```

--------------------------------

### Examine OpenRouter API Usage Object for Prompt Cache Metrics (JSON)

Source: https://openrouter.ai/docs/guides/best-practices/prompt-caching

This JSON example demonstrates the `usage` object returned in OpenRouter API responses, focusing on the `prompt_tokens_details` field. It illustrates how to identify `cached_tokens` (tokens read from cache) and `cache_write_tokens` (tokens written to cache), which are crucial for understanding the cost savings and efficiency gained from prompt caching.

```json
{
  "usage": {
    "prompt_tokens": 10339,
    "completion_tokens": 60,
    "total_tokens": 10399,
    "prompt_tokens_details": {
      "cached_tokens": 10318,
      "cache_write_tokens": 0
    }
  }
}
```

--------------------------------

### Define Get Single API Key Endpoint in OpenAPI

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

This OpenAPI 3.1.1 YAML defines the `/keys/{hash}` GET endpoint for retrieving a single API key. It specifies path and header parameters, details various HTTP responses (200, 401, 404, 429, 500), and outlines the comprehensive schema for the API key data returned in a successful response, including usage, limits, and timestamps.

```yaml
openapi: 3.1.1
info:
  title: Get a single API key
  version: endpoint_apiKeys.getKey
paths:
  /keys/{hash}:
    get:
      operationId: get-key
      summary: Get a single API key
      description: >-
        Get a single API key by hash. [Management
        key](/docs/guides/overview/auth/management-api-keys) required.
      tags:
        - - subpackage_apiKeys
      parameters:
        - name: hash
          in: path
          description: The hash identifier of the API key to retrieve
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: API key details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_getKey_Response_200'
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Not Found - API key does not exist
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    KeysHashGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        hash:
          type: string
          description: Unique hash identifier for the API key
        name:
          type: string
          description: Name of the API key
        label:
          type: string
          description: Human-readable label for the API key
        disabled:
          type: boolean
          description: Whether the API key is disabled
        limit:
          type:
            - number
            - 'null'
          format: double
          description: Spending limit for the API key in USD
        limit_remaining:
          type:
            - number
            - 'null'
          format: double
          description: Remaining spending limit in USD
        limit_reset:
          type:
            - string
            - 'null'
          description: Type of limit reset for the API key
        include_byok_in_limit:
          type: boolean
          description: Whether to include external BYOK usage in the credit limit
        usage:
          type: number
          format: double
          description: Total OpenRouter credit usage (in USD) for the API key
        usage_daily:
          type: number
          format: double
          description: OpenRouter credit usage (in USD) for the current UTC day
        usage_weekly:
          type: number
          format: double
          description: >-
            OpenRouter credit usage (in USD) for the current UTC week
            (Monday-Sunday)
        usage_monthly:
          type: number
          format: double
          description: OpenRouter credit usage (in USD) for the current UTC month
        byok_usage:
          type: number
          format: double
          description: Total external BYOK usage (in USD) for the API key
        byok_usage_daily:
          type: number
          format: double
          description: External BYOK usage (in USD) for the current UTC day
        byok_usage_weekly:
          type: number
          format: double
          description: >-
            External BYOK usage (in USD) for the current UTC week
            (Monday-Sunday)
        byok_usage_monthly:
          type: number
          format: double
          description: External BYOK usage (in USD) for current UTC month
        created_at:
          type: string
          description: ISO 8601 timestamp of when the API key was created
        updated_at:
          type:
            - string
            - 'null'
          description: ISO 8601 timestamp of when the API key was last updated
        expires_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            ISO 8601 UTC timestamp when the API key expires, or null if no
            expiration
      required:
        - hash
        - name
        - label
        - disabled
        - limit
        - limit_remaining
        - limit_reset
        - include_byok_in_limit
        - usage
        - usage_daily
        - usage_weekly
        - usage_monthly
        - byok_usage
        - byok_usage_daily
        - byok_usage_weekly
        - byok_usage_monthly
        - created_at
        - updated_at
    API Keys_getKey_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/KeysHashGetResponsesContentApplicationJsonSchemaData
          description: The API key information
      required:
        - data
```

--------------------------------

### GET /api/v1/models/count

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

Retrieves the total count of available models from OpenRouter. This endpoint requires authentication via bearer token in the Authorization header and returns a JSON response containing the model count.

```APIDOC
## GET /api/v1/models/count

### Description
Get the total count of available models in the OpenRouter catalog.

### Method
GET

### Endpoint
https://openrouter.ai/api/v1/models/count

### Parameters
#### Headers
- **Authorization** (string) - Required - API key as bearer token (format: "Bearer <token>")

### Request Example
```
GET /api/v1/models/count HTTP/1.1
Host: openrouter.ai
Authorization: Bearer <token>
```

### Response
#### Success Response (200)
- **data** (object) - Required - Model count data object
  - **count** (number) - Required - Total number of available models

#### Response Example
```json
{
  "data": {
    "count": 150
  }
}
```

#### Error Response (500)
- **description** - Internal Server Error

### Code Examples

#### Python
```python
import requests

url = "https://openrouter.ai/api/v1/models/count"
headers = {"Authorization": "Bearer <token>"}
response = requests.get(url, headers=headers)
print(response.json())
```

#### JavaScript
```javascript
const url = 'https://openrouter.ai/api/v1/models/count';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

#### Go
```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {
	url := "https://openrouter.ai/api/v1/models/count"
	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Add("Authorization", "Bearer <token>")
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)
	fmt.Println(string(body))
}
```

#### Ruby
```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/models/count")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
response = http.request(request)
puts response.read_body
```

#### Java
```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models/count")
  .header("Authorization", "Bearer <token>")
  .asString();
```

#### PHP
```php
<?php
require_once('vendor/autoload.php');
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'https://openrouter.ai/api/v1/models/count', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);
echo $response->getBody();
```

#### C#
```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/models/count");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

#### Swift
```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]
let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models/count")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})
dataTask.resume()
```
```

--------------------------------

### Define Tool Input Schema with Zod and Descriptions (TypeScript)

Source: https://openrouter.ai/docs/sdks/call-model/tools

This snippet demonstrates how to define a tool's input schema using Zod, incorporating `.describe()` calls to provide human-readable explanations for each parameter. These descriptions help the AI model better understand the purpose and usage of each input, improving tool invocation accuracy. The example defines a search query schema with validation rules and default values.

```typescript
const inputSchema = z.object({
  query: z.string().describe('Natural language search query'),
  maxResults: z.number()
    .min(1)
    .max(100)
    .default(10)
    .describe('Maximum number of results to return (1-100)'),
  dateRange: z.enum(['day', 'week', 'month', 'year', 'all'])
    .default('all')
    .describe('Filter results by time period')
});
```

--------------------------------

### Execute Parallel Tool Calls with OpenRouter AI API (TypeScript, Python)

Source: https://openrouter.ai/docs/api/reference/responses/tool-calling

This example illustrates how to make a single API request to OpenRouter AI that can trigger multiple tool calls in parallel. It shows a user query that requires both a calculation and a weather lookup, demonstrating the API's ability to handle complex requests by invoking multiple tools simultaneously. The `tool_choice` is set to 'auto' to enable this functionality.

```typescript
const response = await fetch('https://openrouter.ai/api/v1/responses', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'openai/o4-mini',
    input: [
      {
        type: 'message',
        role: 'user',
        content: [
          {
            type: 'input_text',
            text: 'Calculate 10*5 and also tell me the weather in Miami',
          },
        ],
      },
    ],
    tools: [weatherTool, calculatorTool],
    tool_choice: 'auto',
    max_output_tokens: 9000,
  }),
});

const result = await response.json();
console.log(result);
```

```python
import requests

response = requests.post(
    'https://openrouter.ai/api/v1/responses',
    headers={
        'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
        'Content-Type': 'application/json',
    },
    json={
        'model': 'openai/o4-mini',
        'input': [
            {
                'type': 'message',
                'role': 'user',
                'content': [
                    {
                        'type': 'input_text',
                        'text': 'Calculate 10*5 and also tell me the weather in Miami',
                    },
                ],
            },
        ],
        'tools': [weather_tool, calculator_tool],
        'tool_choice': 'auto',
        'max_output_tokens': 9000,
    }
)

result = response.json()
print(result)
```

--------------------------------

### Instantiate GetKeyResponse Object in TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getkeyresponse

This code snippet demonstrates how to create an instance of the `GetKeyResponse` object in TypeScript, populating it with example API key data. It illustrates the expected structure of the response, including key details such as hash, name, disabled status, usage limits, and timestamps.

```typescript
import { GetKeyResponse } from "@openrouter/sdk/models/operations";

let value: GetKeyResponse = {
  data: {
    hash: "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943",
    name: "My Production Key",
    label: "Production API Key",
    disabled: false,
    limit: 100,
    limitRemaining: 74.5,
    limitReset: "monthly",
    includeByokInLimit: false,
    usage: 25.5,
    usageDaily: 25.5,
    usageWeekly: 25.5,
    usageMonthly: 25.5,
    byokUsage: 17.38,
    byokUsageDaily: 17.38,
    byokUsageWeekly: 17.38,
    byokUsageMonthly: 17.38,
    createdAt: "2025-08-24T10:30:00Z",
    updatedAt: "2025-08-24T15:45:00Z"
  }
};
```

--------------------------------

### GET /api/v1/generation

Source: https://openrouter.ai/docs/api-reference/get-a-generation

Retrieves request and usage metadata for a specific generation. This endpoint returns detailed information about the generation including costs, latency, token counts, and provider details. Authentication is required via Bearer token.

```APIDOC
## GET /api/v1/generation

### Description
Get request and usage metadata for a generation. Returns comprehensive details about a completed generation including cost breakdown, performance metrics, token usage, and provider information.

### Method
GET

### Endpoint
https://openrouter.ai/api/v1/generation

### Authentication
- **Authorization** (string) - Required - Bearer token in Authorization header format: `Bearer <token>`

### Parameters
#### Query Parameters
- **id** (string) - Required - The generation ID to retrieve metadata for (minimum 1 character)

### Request Example
```
GET https://openrouter.ai/api/v1/generation?id=gen-3bhGkxlo4XFrqiabUM7NDtwDzWwG
Headers:
  Authorization: Bearer <token>
```

### Response
#### Success Response (200 - OK)
- **data** (object) - Generation metadata object containing:
  - **id** (string) - Unique generation identifier
  - **upstream_id** (string) - Provider's upstream request ID
  - **total_cost** (number) - Total cost of the generation
  - **cache_discount** (number) - Discount applied for cached tokens
  - **upstream_inference_cost** (number) - Cost from upstream provider
  - **created_at** (string) - ISO 8601 timestamp of generation creation
  - **model** (string) - Model used for generation
  - **app_id** (integer) - Application ID
  - **streamed** (boolean) - Whether response was streamed
  - **cancelled** (boolean) - Whether generation was cancelled
  - **provider_name** (string) - Name of the inference provider
  - **latency** (integer) - Total latency in milliseconds
  - **moderation_latency** (integer) - Moderation check latency in milliseconds
  - **generation_time** (integer) - Generation time in milliseconds
  - **finish_reason** (string) - Reason generation finished (e.g., "stop")
  - **tokens_prompt** (integer) - Number of prompt tokens
  - **tokens_completion** (integer) - Number of completion tokens
  - **native_tokens_prompt** (integer) - Native prompt tokens
  - **native_tokens_completion** (integer) - Native completion tokens
  - **native_tokens_completion_images** (integer) - Tokens for completion images
  - **native_tokens_reasoning** (integer) - Tokens used for reasoning
  - **native_tokens_cached** (integer) - Cached tokens used
  - **num_media_prompt** (integer) - Number of media items in prompt
  - **num_input_audio_prompt** (integer) - Number of audio inputs in prompt
  - **num_media_completion** (integer) - Number of media items in completion
  - **num_search_results** (integer) - Number of search results used
  - **origin** (string) - Origin URL of the request
  - **usage** (number) - Total usage cost
  - **is_byok** (boolean) - Whether Bring Your Own Key was used
  - **native_finish_reason** (string) - Provider's native finish reason
  - **external_user** (string) - External user identifier
  - **api_type** (string) - Type of API call (e.g., "completions")
  - **router** (string) - Router configuration used
  - **provider_responses** (array) - Array of provider response details

#### Response Example
```json
{
  "data": {
    "id": "gen-3bhGkxlo4XFrqiabUM7NDtwDzWwG",
    "upstream_id": "chatcmpl-791bcf62-080e-4568-87d0-94c72e3b4946",
    "total_cost": 0.0015,
    "cache_discount": 0.0002,
    "upstream_inference_cost": 0.0012,
    "created_at": "2024-07-15T23:33:19.433273+00:00",
    "model": "sao10k/l3-stheno-8b",
    "app_id": 12345,
    "streamed": true,
    "cancelled": false,
    "provider_name": "Infermatic",
    "latency": 1250,
    "moderation_latency": 50,
    "generation_time": 1200,
    "finish_reason": "stop",
    "tokens_prompt": 10,
    "tokens_completion": 25,
    "native_tokens_prompt": 10,
    "native_tokens_completion": 25,
    "native_tokens_completion_images": 0,
    "native_tokens_reasoning": 5,
    "native_tokens_cached": 3,
    "num_media_prompt": 1,
    "num_input_audio_prompt": 0,
    "num_media_completion": 0,
    "num_search_results": 5,
    "origin": "https://openrouter.ai/",
    "usage": 0.0015,
    "is_byok": false,
    "native_finish_reason": "stop",
    "external_user": "user-123",
    "api_type": "completions",
    "router": "openrouter/auto",
    "provider_responses": [
      {
        "status": 1.1,
        "id": "string",
        "endpoint_id": "string",
        "model_permaslug": "string",
        "provider_name": "AnyScale",
        "latency": 1.1,
        "is_byok": true
      }
    ]
  }
}
```

### Error Responses
- **401 Unauthorized** - Invalid or missing authentication token
- **402 Payment Required** - Account has insufficient credits or payment failed
- **404 Not Found** - Generation ID not found
- **429 Too Many Requests** - Rate limit exceeded
- **500 Internal Server Error** - Server-side error occurred
- **502 Bad Gateway** - Upstream service unavailable
```

--------------------------------

### GET /models/{author}/{slug}/endpoints

Source: https://openrouter.ai/docs/sdks/python/api-reference/endpoints

List all endpoints for a model.

```APIDOC
## GET /models/{author}/{slug}/endpoints

### Description
List all endpoints for a model

### Method
GET

### Endpoint
/models/{author}/{slug}/endpoints

### Parameters
#### Path Parameters
- **author** (str) - Required - N/A
- **slug** (str) - Required - N/A

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(None)

### Response
#### Success Response (200)
- **Response Type**: operations.ListEndpointsResponse

#### Response Example
(None)

#### Error Responses
- **404 Not Found**: errors.NotFoundResponseError
- **500 Internal Server Error**: errors.InternalServerResponseError
- **4XX, 5XX Generic Error**: errors.OpenRouterDefaultError
```

--------------------------------

### GET OpenRouter Guardrails API - Swift

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

Performs a GET request to the OpenRouter guardrails API using Swift's URLSession and NSMutableURLRequest. Sets Authorization header with Bearer token and includes error handling in the completion handler.

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create API Key with OpenRouter API - Swift

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

Swift implementation using URLSession and NSMutableURLRequest to create an API key with proper JSON serialization. Includes error handling and demonstrates async data task execution with completion handler.

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "Analytics Service Key",
  "limit": 150,
  "limit_reset": "monthly",
  "include_byok_in_limit": true,
  "expires_at": "2028-06-30T23:59:59Z"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/keys")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Send OpenRouter Chat Completion Request with Custom Headers (TypeScript)

Source: https://openrouter.ai/docs/api-reference/overview

This TypeScript example shows how to make a POST request to the OpenRouter chat completions API, including essential authorization and content type headers. It also demonstrates the use of optional `HTTP-Referer` and `X-Title` headers to identify your application on the OpenRouter platform. These headers help with app discoverability and ranking.

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    Authorization: 'Bearer <OPENROUTER_API_KEY>',
    'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
    'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    model: 'openai/gpt-5.2',
    messages: [
      {
        role: 'user',
        content: 'What is the meaning of life?'
      }
    ]
  })
});
```

--------------------------------

### GET OpenRouter Guardrails API - PHP

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

Makes a GET request to the OpenRouter guardrails API using the Guzzle HTTP client library. Requires Composer autoloader and sets the Authorization header with Bearer token. Outputs the response body.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/guardrails', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

--------------------------------

### GET /guardrails

Source: https://openrouter.ai/docs/sdks/python/api-reference/guardrails

List all guardrails for the authenticated user. This operation requires a provisioning key for authentication.

```APIDOC
## GET /guardrails

### Description
List all guardrails for the authenticated user. This operation requires a provisioning key for authentication.

### Method
GET

### Endpoint
/guardrails

### Parameters
#### Path Parameters
(None)

#### Query Parameters
- **offset** (Optional[str]) - Optional - Number of records to skip for pagination
- **limit** (Optional[str]) - Optional - Maximum number of records to return (max 100)
- **retries** (Optional[utils.RetryConfig]) - Optional - Configuration to override the default retry behavior of the client.

#### Request Body
(None)

### Request Example
{}

### Response
#### Success Response (200)
- **Response Body** (operations.ListGuardrailsResponse) - A list of guardrails.

#### Response Example
{}

### Errors
- **errors.UnauthorizedResponseError** (401) - Unauthorized
- **errors.InternalServerResponseError** (500) - Internal Server Error
- **errors.OpenRouterDefaultError** (4XX, 5XX) - Default error for 4XX or 5XX status codes
```

--------------------------------

### GET /keys/{hash}

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Retrieve details for a single API key using its unique hash identifier. This operation requires a management key for authentication.

```APIDOC
## GET /keys/{hash}

### Description
Get a single API key by hash. [Management key](/docs/guides/overview/auth/management-api-keys) required.

### Method
GET

### Endpoint
/keys/{hash}

### Parameters
#### Path Parameters
- **hash** (string) - Required - The hash identifier of the API key to retrieve

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(None)

### Response
#### Success Response (200)
- **data** (object) - The API key information
  - **hash** (string) - Unique hash identifier for the API key
  - **name** (string) - Name of the API key
  - **label** (string) - Human-readable label for the API key
  - **disabled** (boolean) - Whether the API key is disabled
  - **limit** (number/null) - Spending limit for the API key in USD
  - **limit_remaining** (number/null) - Remaining spending limit in USD
  - **limit_reset** (string/null) - Type of limit reset for the API key
  - **include_byok_in_limit** (boolean) - Whether to include external BYOK usage in the credit limit
  - **usage** (number) - Total OpenRouter credit usage (in USD) for the API key
  - **usage_daily** (number) - OpenRouter credit usage (in USD) for the current UTC day
  - **usage_weekly** (number) - OpenRouter credit usage (in USD) for the current UTC week (Monday-Sunday)
  - **usage_monthly** (number) - OpenRouter credit usage (in USD) for the current UTC month
  - **byok_usage** (number) - Total external BYOK usage (in USD) for the API key
  - **byok_usage_daily** (number) - External BYOK usage (in USD) for the current UTC day
  - **byok_usage_weekly** (number) - External BYOK usage (in USD) for the current UTC week (Monday-Sunday)
  - **byok_usage_monthly** (number) - External BYOK usage (in USD) for current UTC month
  - **created_at** (string) - ISO 8601 timestamp of when the API key was created
  - **updated_at** (string/null) - ISO 8601 timestamp of when the API key was last updated
  - **expires_at** (string/null) - ISO 8601 UTC timestamp when the API key expires, or null if no expiration

#### Response Example
```json
{
  "data": {
    "hash": "some_api_key_hash",
    "name": "My API Key",
    "label": "Development Key",
    "disabled": false,
    "limit": 100.0,
    "limit_remaining": 75.5,
    "limit_reset": "monthly",
    "include_byok_in_limit": true,
    "usage": 24.5,
    "usage_daily": 1.2,
    "usage_weekly": 5.8,
    "usage_monthly": 24.5,
    "byok_usage": 10.0,
    "byok_usage_daily": 0.5,
    "byok_usage_weekly": 2.0,
    "byok_usage_monthly": 10.0,
    "created_at": "2023-01-01T10:00:00Z",
    "updated_at": "2023-01-05T15:30:00Z",
    "expires_at": null
  }
}
```
```

--------------------------------

### GET OpenRouter Guardrails API - Ruby

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

Uses Ruby's Net::HTTP library to make a GET request to the OpenRouter guardrails API with SSL enabled. Sets the Authorization header with Bearer token and outputs the response body.

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/guardrails")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

--------------------------------

### Initialize OpenRouter Client with API Key

Source: https://openrouter.ai/docs/sdks/python/overview

Create an OpenRouter client instance using context manager pattern with API key from environment variables. This establishes a connection to the OpenRouter API for making requests to language models.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY")
) as client:
    response = client.chat.send(
        model="minimax/minimax-m2",
        messages=[
            {"role": "user", "content": "Explain quantum computing"}
        ]
    )
```

--------------------------------

### Integrate OpenRouter DevTools hooks for basic telemetry capture (TypeScript)

Source: https://openrouter.ai/docs/sdks/dev-tools/devtools

This TypeScript example demonstrates the basic integration of `createOpenRouterDevtools` into an OpenRouter SDK client. Once integrated, all subsequent SDK operations, such as chat completions, will automatically capture telemetry data for debugging and visualization.

```typescript
import { createOpenRouterDevtools } from '@openrouter/devtools';
import { OpenRouter } from '@openrouter/sdk';

const sdk = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
  hooks: createOpenRouterDevtools()
});

// Now all SDK operations are automatically captured
const response = await sdk.chat.send({
  model: "openai/gpt-5",
  messages: [
    { role: "user", content: "Explain quantum computing" }
  ]
});
```

--------------------------------

### GET /guardrails

Source: https://openrouter.ai/docs/sdks/python/api-reference/operations/listguardrailsresponse

This endpoint retrieves a list of available guardrails, providing details about each guardrail and the total count of guardrails.

```APIDOC
## GET /guardrails

### Description
This endpoint retrieves a list of available guardrails. It provides details about each guardrail and the total count of guardrails.

### Method
GET

### Endpoint
/guardrails

### Parameters
#### Path Parameters
No path parameters.

#### Query Parameters
No query parameters.

#### Request Body
No request body.

### Request Example
No request body for this GET endpoint.

### Response
#### Success Response (200)
- **data** (array of objects) - Required - List of guardrail objects. Each object contains details about a specific guardrail, such as its ID, name, and status.
- **total_count** (float) - Required - The total number of guardrails available.

#### Response Example
{
  "data": [
    {
      "id": "content_moderation",
      "name": "Content Moderation Guardrail",
      "status": "active",
      "type": "safety"
    },
    {
      "id": "pii_detection",
      "name": "PII Detection Guardrail",
      "status": "inactive",
      "type": "privacy"
    }
  ],
  "total_count": 2.0
}
```

--------------------------------

### GET /embeddings/models

Source: https://openrouter.ai/docs/sdks/python/api-reference/embeddings

Returns a list of all available embeddings models and their properties.

```APIDOC
## GET /embeddings/models

### Description
Returns a list of all available embeddings models and their properties.

### Method
GET

### Endpoint
/embeddings/models

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
{}

### Response
#### Success Response (200)
- **Response Type** (object) - A `components.ModelsListResponse` object containing an array of available embeddings models.

#### Response Example
```json
{
  "data": [
    {
      "id": "openai/text-embedding-ada-002",
      "name": "text-embedding-ada-002",
      "provider": {
        "id": "openai",
        "name": "OpenAI"
      },
      "context_length": 8191,
      "pricing": {
        "prompt": "0.0000001",
        "completion": "0.0000000"
      },
      "architecture": {
        "modality": "text",
        "tokenizer": "tiktoken",
        "instruct_type": "none"
      },
      "per_request_limits": {
        "prompt_tokens": 8191,
        "completion_tokens": 0
      },
      "top_providers": [
        {
          "id": "openai",
          "name": "OpenAI"
        }
      ]
    },
    {
      "id": "google/embedding-gecko",
      "name": "embedding-gecko",
      "provider": {
        "id": "google",
        "name": "Google"
      },
      "context_length": 1024,
      "pricing": {
        "prompt": "0.0000002",
        "completion": "0.0000000"
      },
      "architecture": {
        "modality": "text",
        "tokenizer": "google",
        "instruct_type": "none"
      },
      "per_request_limits": {
        "prompt_tokens": 1024,
        "completion_tokens": 0
      },
      "top_providers": [
        {
          "id": "google",
          "name": "Google"
        }
      ]
    }
  ]
}
```

### Errors
#### Bad Request (400)
- **Type** (string) - `errors.BadRequestResponseError`
- **Content Type** (string) - `application/json`
- **Description** - The request was malformed or invalid.

#### Internal Server Error (500)
- **Type** (string) - `errors.InternalServerResponseError`
- **Content Type** (string) - `application/json`
- **Description** - An unexpected error occurred on the server.

#### OpenRouter Default Error (4XX, 5XX)
- **Type** (string) - `errors.OpenRouterDefaultError`
- **Content Type** (string) - `*/*`
- **Description** - Generic error for other client or server-side issues.
```

--------------------------------

### Configure AI Skill with Custom Options in TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

This TypeScript tool allows loading an AI skill with custom configuration options such as verbosity, strict mode, and output format. It dynamically generates a configuration header within the model's input context and can adjust model parameters, like temperature, based on the provided skill options.

```typescript
const configurableSkillLoader = tool({
  name: 'configure_skill',
  description: 'Load a skill with custom configuration options',

  inputSchema: z.object({
    skillName: z.string(),
    options: z
      .object({
        verbosity: z.enum(['minimal', 'normal', 'detailed']).default('normal'),
        strictMode: z.boolean().default(false),
        outputFormat: z.enum(['json', 'markdown', 'plain']).default('markdown'),
      })
      .optional(),
  }),

  outputSchema: z.object({
    status: z.enum(['loaded', 'already_loaded', 'not_found']),
    message: z.string(),
    configuration: z.record(z.unknown()).optional(),
  }),

  nextTurnParams: {
    input: (params, context) => {
      const skillMarker = `[Skill: ${params.skillName}]`;
      if (JSON.stringify(context.input).includes(skillMarker)) {
        return context.input;
      }

      const skillPath = path.join(SKILLS_DIR, params.skillName, 'SKILL.md');
      if (!existsSync(skillPath)) {
        return context.input;
      }

      const skillContent = readFileSync(skillPath, 'utf-8');
      const options = params.options || {};

      // Build configuration header
      const configHeader = `
## Skill Configuration
- Verbosity: ${options.verbosity || 'normal'}
- Strict Mode: ${options.strictMode || false}
- Output Format: ${options.outputFormat || 'markdown'}
`;

      const currentInput = Array.isArray(context.input) ? context.input : [context.input];

      return [
        ...currentInput,
        {
          role: 'user',
          content: `${skillMarker}
${configHeader}

${skillContent}`,
        },
      ];
    },

    // Adjust model behavior based on skill
    temperature: (params, context) => {
      // Lower temperature for strict mode
      if (params.options?.strictMode) {
        return 0.3;
      }
      return context.temperature;
    },
  },

  execute: async ({ skillName, options }) => {
    const skillPath = path.join(SKILLS_DIR, skillName, 'SKILL.md');

    if (!existsSync(skillPath)) {
      return {
        status: 'not_found' as const,
        message: `Skill "${skillName}" not found`,
      };
    }

    return {
      status: 'loaded' as const,
      message: `Skill "${skillName}" loaded with configuration`,
      configuration: options || {},
    };
  },
});
```

--------------------------------

### Best Practice: Keep Dynamic Parameter Functions Pure and Avoid Side Effects in OpenRouter AI (JavaScript)

Source: https://openrouter.ai/docs/sdks/call-model/dynamic-parameters

This snippet illustrates the best practice of using pure functions for dynamic parameters in OpenRouter AI, showing a good example of conditional model selection and an example to avoid that introduces side effects like logging to a database.

```javascript
// Good: Pure function  
model: (ctx) => ctx.numberOfTurns > 3 ? 'gpt-4' : 'gpt-4o-mini',
  
// Avoid: Side effects  
model: (ctx) => {
  logToDatabase(ctx); // Side effect  
  return 'gpt-4';
},
```

--------------------------------

### List Guardrail Key Assignments using OpenRouter SDK (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/guardrails

This example demonstrates how to list API key assignments for a specific guardrail using the main OpenRouter SDK. It initializes the SDK with an API key and then calls the `listGuardrailKeyAssignments` method on the `guardrails` object, providing the guardrail's unique identifier.

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.guardrails.listGuardrailKeyAssignments({
    id: "550e8400-e29b-41d4-a716-446655440000",
  });

  console.log(result);
}

run();
```

--------------------------------

### Get Remaining Credits - Python HTTP Request

Source: https://openrouter.ai/docs/api-reference/get-credits

Fetch remaining credits for authenticated user using Python requests library. Requires Bearer token in Authorization header. Returns JSON object containing total_credits and total_usage properties.

```python
import requests

url = "https://openrouter.ai/api/v1/credits"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

--------------------------------

### Sort OpenRouter Models by Price using Floor Shortcut

Source: https://openrouter.ai/docs/guides/routing/provider-selection

This code illustrates how to sort OpenRouter models by price using the `:floor` shortcut. Appending `:floor` to the model slug ensures that requests prioritize providers with lower prices. This is equivalent to setting `provider.sort` to `"price"`.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
});

const completion = await openRouter.chat.send({
  model: 'meta-llama/llama-3.3-70b-instruct:floor',
  messages: [{ role: 'user', content: 'Hello' }],
  stream: false,
});
```

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer <OPENROUTER_API_KEY>',
    'HTTP-Referer': '<YOUR_SITE_URL>',
    'X-Title': '<YOUR_SITE_NAME>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'meta-llama/llama-3.3-70b-instruct:floor',
    messages: [{ role: 'user', content: 'Hello' }],
  }),
});
```

```python
import requests

headers = {
  'Authorization': 'Bearer <OPENROUTER_API_KEY>',
  'HTTP-Referer': '<YOUR_SITE_URL>',
  'X-Title': '<YOUR_SITE_NAME>',
  'Content-Type': 'application/json',
}

response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
  'model': 'meta-llama/llama-3.3-70b-instruct:floor',
  'messages': [{ 'role': 'user', 'content': 'Hello' }],
})
```

--------------------------------

### Retrieve API Key Information - C#

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key

Makes an authenticated GET request using RestSharp library. Constructs REST client with endpoint URL and adds Bearer token to request headers.

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/key");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create ListResponse object with API keys - TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listresponse

Demonstrates how to create a ListResponse object containing API key data with usage statistics, limits, and timestamps. The example shows a production API key with monthly limits, daily/weekly/monthly usage tracking, and BYOK (Bring Your Own Key) usage metrics.

```typescript
import { ListResponse } from "@openrouter/sdk/models/operations";

let value: ListResponse = {
  data: [
    {
      hash: "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943",
      name: "My Production Key",
      label: "Production API Key",
      disabled: false,
      limit: 100,
      limitRemaining: 74.5,
      limitReset: "monthly",
      includeByokInLimit: false,
      usage: 25.5,
      usageDaily: 25.5,
      usageWeekly: 25.5,
      usageMonthly: 25.5,
      byokUsage: 17.38,
      byokUsageDaily: 17.38,
      byokUsageWeekly: 17.38,
      byokUsageMonthly: 17.38,
      createdAt: "2025-08-24T10:30:00Z",
      updatedAt: "2025-08-24T15:45:00Z"
    }
  ]
};
```

--------------------------------

### Implement Progressive Model Upgrade in OpenRouter SDK

Source: https://openrouter.ai/docs/sdks/typescript/call-model/dynamic-parameters

This snippet demonstrates a common pattern for progressive model upgrading. It starts with a faster, less resource-intensive model for the initial turns and switches to a more capable model for complex tasks or longer conversations, optimizing both performance and quality.

```typescript
const result = openrouter.callModel({
  model: (ctx) => {
    // First few turns: fast model
    if (ctx.numberOfTurns <= 2) {
      return 'openai/gpt-5-nano';
    }

    // Complex conversations: capable model
    return 'openai/gpt-5.2';
  },
  input: 'Let me think through this problem...',
  tools: [analysisTool],
});
```

--------------------------------

### Define Get Guardrail Endpoint in OpenAPI Specification

Source: https://openrouter.ai/docs/api/api-reference/guardrails/get-guardrail

This OpenAPI 3.1.1 specification defines the GET /guardrails/{id} endpoint for retrieving a single guardrail. It details the path parameter `id`, required `Authorization` header, and expected responses including success (200) with guardrail details and error cases (401, 404, 500). It also defines the schema for the guardrail object, including properties like `id`, `name`, `description`, `limit_usd`, `reset_interval`, `allowed_providers`, `allowed_models`, `enforce_zdr`, `created_at`, and `updated_at`.

```yaml
openapi: 3.1.1
info:
  title: Get a guardrail
  version: endpoint_guardrails.getGuardrail
paths:
  /guardrails/{id}:
    get:
      operationId: get-guardrail
      summary: Get a guardrail
      description: >-
        Get a single guardrail by ID. [Management
        key](/docs/guides/overview/auth/management-api-keys) required.
      tags:
        - - subpackage_guardrails
      parameters:
        - name: id
          in: path
          description: The unique identifier of the guardrail to retrieve
          required: true
          schema:
            type: string
            format: uuid
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Guardrail details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Guardrails_getGuardrail_Response_200'
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Not Found - Guardrail does not exist
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    GuardrailsIdGetResponsesContentApplicationJsonSchemaDataResetInterval:
      type: string
      enum:
        - value: daily
        - value: weekly
        - value: monthly
    GuardrailsIdGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the guardrail
        name:
          type: string
          description: Name of the guardrail
        description:
          type:
            - string
            - 'null'
          description: Description of the guardrail
        limit_usd:
          type:
            - number
            - 'null'
          format: double
          description: Spending limit in USD
        reset_interval:
          oneOf:
            - $ref: >-
                #/components/schemas/GuardrailsIdGetResponsesContentApplicationJsonSchemaDataResetInterval
            - type: 'null'
          description: Interval at which the limit resets (daily, weekly, monthly)
        allowed_providers:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of allowed provider IDs
        allowed_models:
          type:
            - array
            - 'null'
          items:
            type: string
          description: Array of model canonical_slugs (immutable identifiers)
        enforce_zdr:
          type:
            - boolean
            - 'null'
          description: Whether to enforce zero data retention
        created_at:
          type: string
          description: ISO 8601 timestamp of when the guardrail was created
        updated_at:
          type:
            - string
            - 'null'
          description: ISO 8601 timestamp of when the guardrail was last updated
      required:
        - id
        - name
        - created_at
    Guardrails_getGuardrail_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/GuardrailsIdGetResponsesContentApplicationJsonSchemaData
          description: The guardrail
      required:
        - data
```

--------------------------------

### GET /providers

Source: https://openrouter.ai/docs/sdks/python/api-reference/providers

This endpoint allows you to retrieve a list of all available providers. It provides an overview of the provider information.

```APIDOC
## GET /providers

### Description
List all providers

### Method
GET

### Endpoint
/providers

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
{}

### Response
#### Success Response (200)
- **Response Body** (object) - A `ListProvidersResponse` object containing details of all available providers. Specific fields are defined in `operations.ListProvidersResponse`.

#### Response Example
{
  "example": "Response structure for ListProvidersResponse not provided in the input text."
}
```

--------------------------------

### GET /api/v1/guardrails/assignments/keys

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-key-assignments

This endpoint retrieves a paginated list of all API key guardrail assignments for the authenticated user. A management key is required for authentication.

```APIDOC
## GET /api/v1/guardrails/assignments/keys

### Description
List all API key guardrail assignments for the authenticated user. A management key is required.

### Method
GET

### Endpoint
/api/v1/guardrails/assignments/keys

### Parameters
#### Query Parameters
- **offset** (string) - Optional - Number of records to skip for pagination.
- **limit** (string) - Optional - Maximum number of records to return (max 100).

#### Header Parameters
- **Authorization** (string) - Required - API key as bearer token in Authorization header.

### Response
#### Success Response (200)
- **data** (array) - List of key assignments.
  - **id** (string) - Unique identifier for the assignment.
  - **key_hash** (string) - Hash of the assigned API key.
  - **guardrail_id** (string) - ID of the guardrail.
  - **key_name** (string) - Name of the API key.
  - **key_label** (string) - Label of the API key.
  - **assigned_by** (string/null) - User ID of who made the assignment.
  - **created_at** (string) - ISO 8601 timestamp of when the assignment was created.
- **total_count** (number) - Total number of key assignments for this guardrail.

#### Response Example
```json
{
  "data": [
    {
      "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
      "key_hash": "sha256:examplehash",
      "guardrail_id": "b1c2d3e4-f5a6-8901-2345-67890abcdef0",
      "key_name": "My API Key",
      "key_label": "Development Key",
      "assigned_by": "user-id-123",
      "created_at": "2023-10-27T10:00:00Z"
    }
  ],
  "total_count": 1
}
```
```

--------------------------------

### Delete Guardrail - Go Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/delete-guardrail

Go implementation using the net/http package to send a DELETE request to remove a guardrail.

```APIDOC
### Go Example

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {
	url := "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))
}
```
```

--------------------------------

### Example OpenRouter API Request with Arize Trace Metadata (JSON)

Source: https://openrouter.ai/docs/guides/features/broadcast/arize

This JSON example demonstrates an OpenRouter API request payload including custom `trace` metadata. This metadata is used by Arize AI to organize and enrich traces, mapping specific keys like `trace_id`, `trace_name`, `generation_name`, `dataset`, and `experiment_id` to span attributes in the OTLP payload. The `user` and `session_id` fields are also mapped to user and session identification attributes respectively.

```json
{
  "model": "openai/gpt-4o",
  "messages": [{ "role": "user", "content": "Classify this text..." }],
  "user": "user_12345",
  "session_id": "session_abc",
  "trace": {
    "trace_id": "classification_pipeline_001",
    "trace_name": "Text Classification",
    "generation_name": "Classify Sentiment",
    "dataset": "customer_feedback",
    "experiment_id": "exp_v3"
  }
}
```

--------------------------------

### Define and Automatically Execute a Tool in OpenRouter SDK

Source: https://openrouter.ai/docs/sdks/typescript/call-model/tools

This comprehensive example demonstrates defining a tool with `zod` for schema validation and an asynchronous `execute` function. It shows how the `callModel` method automatically handles the execution of the tool, and `getText()` waits for all tool interactions to complete before returning the final model response.

```typescript
import { OpenRouter, tool } from '@openrouter/sdk';
import { z } from 'zod';

const weatherTool = tool({
  name: 'get_weather',
  inputSchema: z.object({ location: z.string() }),
  outputSchema: z.object({ temperature: z.number() }),
  execute: async ({ location }) => {
    return { temperature: await fetchTemperature(location) };
  },
});

const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  input: 'What is the weather in Paris?',
  tools: [weatherTool],
});

// getText() waits for all tool execution to complete
const text = await result.getText();
// "The weather in Paris is 18°C."
```

--------------------------------

### Construct OpenRouter Authorization URL for PKCE

Source: https://openrouter.ai/docs/guides/overview/auth/oauth

This snippet demonstrates how to construct the authorization URL to redirect users to OpenRouter for authentication. It includes variations for S256 (recommended), plain code challenge, and no code challenge methods. The `callback_url` is where the user will be redirected after authorization.

```txt
https://openrouter.ai/auth?callback_url=<YOUR_SITE_URL>&code_challenge=<CODE_CHALLENGE>&code_challenge_method=S256
```

```txt
https://openrouter.ai/auth?callback_url=<YOUR_SITE_URL>&code_challenge=<CODE_CHALLENGE>&code_challenge_method=plain
```

```txt
https://openrouter.ai/auth?callback_url=<YOUR_SITE_URL>
```

--------------------------------

### Test Weather Tool Functionality with Bun Test Framework in TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/weather-tool

This snippet demonstrates how to write unit tests for a weather tool using Bun's built-in test framework. It shows how to mock the global `fetch` function to simulate API responses, allowing for isolated testing of the tool's logic. Tests cover successful data retrieval for a valid city and error handling for scenarios like 'city not found', ensuring the tool behaves correctly under various conditions.

```typescript
import { describe, it, expect, mock } from 'bun:test';

describe('weatherTool', () => {
  it('returns weather data for valid city', async () => {
    // Mock the fetch response
    global.fetch = mock(() =>
      Promise.resolve({
        ok: true,
        json: () =>
          Promise.resolve({
            current: {
              temp_c: 22,
              temp_f: 72,
              feelslike_c: 24,
              feelslike_f: 75,
              condition: { text: 'Sunny' },
              humidity: 45,
              wind_kph: 10,
              wind_dir: 'NW',
            },
            location: {
              name: 'London',
              region: 'City of London',
              country: 'UK',
            },
          }),
      })
    );

    const result = await weatherTool.function.execute(
      { city: 'London', units: 'celsius' },
      { numberOfTurns: 1 }
    );

    expect(result.temperature).toBe(22);
    expect(result.conditions).toBe('Sunny');
    expect(result.location.name).toBe('London');
  });

  it('handles city not found', async () => {
    global.fetch = mock(() =>
      Promise.resolve({
        ok: false,
        status: 400,
      })
    );

    await expect(
      weatherTool.function.execute(
        { city: 'InvalidCity123', units: 'celsius' },
        { numberOfTurns: 1 }
      )
    ).rejects.toThrow('City not found');
  });
});
```

--------------------------------

### Fetch Models List - Python with Requests

Source: https://openrouter.ai/docs/api/api-reference/models/get-models

Makes a GET request to the OpenRouter models endpoint using the requests library. Requires a valid Bearer token for authentication. Returns JSON response containing the list of available AI models.

```python
import requests

url = "https://openrouter.ai/api/v1/models"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

--------------------------------

### GET /auth (Initiate OAuth PKCE Flow)

Source: https://openrouter.ai/docs/guides/overview/auth/oauth

Redirects the user to OpenRouter's authorization page to initiate the OAuth PKCE flow. The user will be prompted to log in and authorize the application, then redirected back to the provided `callback_url` with an authorization `code`.

```APIDOC
## GET /auth

### Description
Redirects the user to OpenRouter's authorization page to initiate the OAuth PKCE flow. The user will be prompted to log in and authorize the application, then redirected back to the provided `callback_url` with an authorization `code`.

### Method
GET

### Endpoint
https://openrouter.ai/auth

### Parameters
#### Path Parameters
(None)

#### Query Parameters
- **callback_url** (string) - Required - The URL on your site where the user will be redirected after authorization.
- **code_challenge** (string) - Optional - A cryptographically random string used to prevent authorization code interception attacks. Recommended for security.
- **code_challenge_method** (string) - Optional - The method used to generate the `code_challenge`. Recommended: `S256`. Other option: `plain`.

#### Request Body
(None)

### Request Example
https://openrouter.ai/auth?callback_url=https://your-app.com/auth/callback&code_challenge=YOUR_CODE_CHALLENGE&code_challenge_method=S256

### Response
#### Success Response (302 Redirect)
- User is redirected to `callback_url` with `code` query parameter.

#### Response Example
https://your-app.com/auth/callback?code=YOUR_AUTHORIZATION_CODE
```

--------------------------------

### GET /generation

Source: https://openrouter.ai/docs/api/api-reference/generations/get-generation

Retrieves the request and usage metadata for a specific generation. This endpoint requires a generation ID and an API key for authentication.

```APIDOC
## GET /generation

### Description
Get request and usage metadata for a specific generation. This endpoint provides details about the generation process, including provider responses and status.

### Method
GET

### Endpoint
/generation

### Parameters
#### Query Parameters
- **id** (string) - Required - The unique identifier of the generation.

#### Header Parameters
- **Authorization** (string) - Required - API key as bearer token (e.g., `Bearer YOUR_API_KEY`).

### Request Example
{}

### Response
#### Success Response (200)
- **description** (string) - Returns the request metadata for this generation.
- **data** (object) - The generation metadata object.
  - **api_type** (string) - Type of API used for the generation (e.g., `completions`, `embeddings`).
  - **provider_responses** (array) - A list of responses from the underlying providers.
    - **id** (string) - Unique identifier for the provider response.
    - **endpoint_id** (string) - Identifier for the endpoint used.
    - **model_permaslug** (string) - Permanent slug for the model used.
    - **provider_name** (string) - Name of the AI provider (e.g., `OpenAI`, `Anthropic`).
    - **status** (number or null) - HTTP status code returned by the provider.
    - **latency** (number) - Latency of the provider's response in milliseconds.

#### Error Responses
- **401 Unauthorized**: Authentication required or invalid credentials.
- **402 Payment Required**: Insufficient credits or quota to complete request.
- **404 Not Found**: Generation not found.
- **429 Too Many Requests**: Rate limit exceeded.
- **500 Internal Server Error**: Unexpected server error.
- **502 Bad Gateway**: Provider/upstream API failure.

#### Response Example
{
  "description": "Returns the request metadata for this generation",
  "data": {
    "api_type": "completions",
    "provider_responses": [
      {
        "id": "pr_example123",
        "endpoint_id": "ep_example456",
        "model_permaslug": "openai/gpt-4",
        "provider_name": "OpenAI",
        "status": 200,
        "latency": 150.5
      }
    ]
  }
}
```

--------------------------------

### Assistant Prefill

Source: https://openrouter.ai/docs/api-reference/overview

Guide model responses by providing a partial assistant message. This feature allows you to control the format and direction of model completions by including an assistant role message in your messages array.

```APIDOC
## Assistant Prefill

### Description
OpenRouter supports asking models to complete a partial response. This can be useful for guiding models to respond in a certain way or to establish a specific tone and format.

### Method
Include a message with `role: "assistant"` at the end of your `messages` array to provide a prefill that the model will complete.

### Request Body
- **messages** (array) - Required - Array of message objects
  - Include a final message with `role: "assistant"` containing the partial response to complete

### Request Example
```
{
  "model": "openai/gpt-5.2",
  "messages": [
    {
      "role": "user",
      "content": "What is the meaning of life?"
    },
    {
      "role": "assistant",
      "content": "I'm not sure, but my best guess is"
    }
  ]
}
```

### Use Cases
- Guide models to respond in a specific format
- Establish tone and style for responses
- Control the direction of model completions
- Ensure responses follow a particular structure

### Notes
- The prefill content will be completed by the model
- The model will continue from where the prefill ends
- This works with all supported models
```

--------------------------------

### Create API Key with OpenRouter API - Ruby

Source: https://openrouter.ai/docs/api/api-reference/api-keys/create-keys

Ruby implementation using Net::HTTP library to create an API key with SSL/TLS support. Constructs a POST request with proper headers and JSON body, then executes the request and outputs the response.

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Analytics Service Key\",\n  \"limit\": 150,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true,\n  \"expires_at\": \"2028-06-30T23:59:59Z\"\n}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Fetch OpenRouter API Keys - Ruby

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Uses Ruby's Net::HTTP library to make an HTTPS GET request with Bearer token authentication. Handles SSL connection and prints the response body.

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

--------------------------------

### Delete Guardrail - Ruby Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/delete-guardrail

Ruby implementation using Net::HTTP to delete a guardrail with SSL support.

```APIDOC
### Ruby Example

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```
```

--------------------------------

### Fetch OpenRouter Guardrail Data (Multi-language)

Source: https://openrouter.ai/docs/api/api-reference/guardrails/get-guardrail

These code snippets demonstrate how to make a GET request to the OpenRouter API's guardrails endpoint to retrieve specific guardrail information. The request requires an Authorization header with a Bearer token. The output is typically a JSON response containing the guardrail data.

```python
import requests

url = "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### GET /credits

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/credits

This endpoint retrieves the total credits purchased and used for the authenticated user. A provisioning key is required for authentication.

```APIDOC
## GET /credits

### Description
Retrieves the total credits purchased and used for the authenticated user.

### Method
GET

### Endpoint
/credits

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(GET requests typically do not have a request body.)

### Response
#### Success Response (200)
- **total_credits** (number) - Total credits purchased by the user.
- **used_credits** (number) - Credits consumed by the user.
- **remaining_credits** (number) - Credits remaining for the user.
- **currency** (string) - The currency in which credits are denominated (e.g., "USD").

#### Response Example
```json
{
  "total_credits": 1000,
  "used_credits": 250,
  "remaining_credits": 750,
  "currency": "USD"
}
```

#### Error Responses
- **401 Unauthorized** - Invalid or missing authentication credentials.
- **403 Forbidden** - User does not have permission to access this resource.
- **500 Internal Server Error** - An unexpected error occurred on the server.
- **4XX, 5XX OpenRouterDefaultError** - Generic error for client or server issues.
```

--------------------------------

### Query Custom Metadata in OpenRouter Traces

Source: https://openrouter.ai/docs/guides/features/broadcast/grafana

TraceQL query to filter traces by custom metadata attributes sent with OpenRouter requests. This example queries traces from the production environment using the trace.metadata namespace.

```traceql
{ resource.service.name = "openrouter" && span.trace.metadata.environment = "production" }
```

--------------------------------

### GET /keys/{hash}

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/apikeys

Retrieves details for a single API key using its hash. A provisioning key is required for this operation.

```APIDOC
## GET /keys/{hash}

### Description
Retrieves details for a single API key using its hash. A provisioning key is required for this operation.

### Method
GET

### Endpoint
/keys/{hash}

### Parameters
#### Path Parameters
- **hash** (string) - Required - The unique hash identifier of the API key to retrieve.

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(No request body for GET, path parameter is in URL)

### Response
#### Success Response (200)
- **id** (string) - The unique identifier of the API key.
- **hash** (string) - The hash of the API key.
- **created_at** (string) - Timestamp when the API key was created (ISO 8601 format).
- **expires_at** (string, optional) - Timestamp when the API key expires (ISO 8601 format).
- **status** (string) - Current status of the API key (e.g., "active", "revoked").
- **metadata** (object, optional) - Additional metadata associated with the key.

#### Response Example
```json
{
  "id": "key_abc123",
  "hash": "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943",
  "created_at": "2023-10-27T10:00:00Z",
  "expires_at": null,
  "status": "active",
  "metadata": {}
}
```

### Errors
- **401 UnauthorizedResponseError**: The request is not authorized.
- **404 NotFoundResponseError**: The API key with the specified hash was not found.
- **429 TooManyRequestsResponseError**: Too many requests have been made in a given amount of time.
- **500 InternalServerResponseError**: An unexpected error occurred on the server.
- **4XX, 5XX OpenRouterDefaultError**: Generic client or server error.
```

--------------------------------

### Define and Use Multiple Tools with OpenRouter AI API (TypeScript, Python)

Source: https://openrouter.ai/docs/api/reference/responses/tool-calling

This snippet demonstrates how to define multiple tools (e.g., a calculator tool) and include them in a single API request to OpenRouter AI. It shows how to structure tool definitions and pass them in the `tools` array for complex workflows. Note that `weatherTool` is referenced but not defined in this snippet, implying it's defined elsewhere.

```typescript
const calculatorTool = {
  type: 'function' as const,
  name: 'calculate',
  description: 'Perform mathematical calculations',
  strict: null,
  parameters: {
    type: 'object',
    properties: {
      expression: {
        type: 'string',
        description: 'The mathematical expression to evaluate',
      },
    },
    required: ['expression'],
  },
};

const response = await fetch('https://openrouter.ai/api/v1/responses', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'openai/o4-mini',
    input: [
      {
        type: 'message',
        role: 'user',
        content: [
          {
            type: 'input_text',
            text: 'What is 25 * 4?',
          },
        ],
      },
    ],
    tools: [weatherTool, calculatorTool],
    tool_choice: 'auto',
    max_output_tokens: 9000,
  }),
});
```

```python
calculator_tool = {
    'type': 'function',
    'name': 'calculate',
    'description': 'Perform mathematical calculations',
    'strict': None,
    'parameters': {
        'type': 'object',
        'properties': {
            'expression': {
                'type': 'string',
                'description': 'The mathematical expression to evaluate',
            },
        },
        'required': ['expression'],
    },
}

response = requests.post(
    'https://openrouter.ai/api/v1/responses',
    headers={
        'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
        'Content-Type': 'application/json',
    },
    json={
        'model': 'openai/o4-mini',
        'input': [
            {
                'type': 'message',
                'role': 'user',
                'content': [
                    {
                        'type': 'input_text',
                        'text': 'What is 25 * 4?',
                    },
                ],
            },
        ],
        'tools': [weather_tool, calculator_tool],
        'tool_choice': 'auto',
        'max_output_tokens': 9000,
    }
)
```

--------------------------------

### List Providers with Standalone Function (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/providers

This example illustrates using the standalone `providersList` function from `@openrouter/sdk/funcs/providersList.js` for optimized tree-shaking. It initializes `OpenRouterCore`, executes the function, and includes error handling for the API call.

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { providersList } from "@openrouter/sdk/funcs/providersList.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await providersList(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("providersList failed:", res.error);
  }
}

run();
```

--------------------------------

### Legacy Parameters

Source: https://openrouter.ai/docs/best-practices/reasoning-tokens

Documents backward-compatible legacy parameters for reasoning configuration. These parameters are still supported but the new unified reasoning parameter is recommended for better control and future compatibility.

```APIDOC
## Legacy Parameters

### Description
OpenRouter maintains backward compatibility with legacy reasoning parameters. These are equivalent to the new unified `reasoning` parameter but with limited functionality.

### Supported Legacy Parameters
- **include_reasoning: true** - Equivalent to `reasoning: {}`
  - Enables reasoning with default settings
- **include_reasoning: false** - Equivalent to `reasoning: { exclude: true }`
  - Disables reasoning in the response

### Recommendation
Use the new unified `reasoning` parameter for better control and future compatibility instead of legacy parameters.
```

--------------------------------

### Delete Guardrail - PHP Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/delete-guardrail

PHP implementation using Guzzle HTTP client to delete a guardrail.

```APIDOC
### PHP Example

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```
```

--------------------------------

### Send API Request to OpenRouter AI - JavaScript

Source: https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages

JavaScript example using the Fetch API to send a POST request to OpenRouter AI's messages endpoint. Includes error handling with try-catch block and async/await pattern for handling the response.

```javascript
const url = 'https://openrouter.ai/api/v1/messages';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"model":"anthropic/claude-4.5-sonnet-20250929","max_tokens":1024,"messages":[{"role":"user","content":"Hello, how are you?"}],"temperature":0.7}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

--------------------------------

### GET /models

Source: https://openrouter.ai/docs/overview/models

Retrieves a list of all available language models with their comprehensive metadata, including architecture, pricing, and supported parameters. The response is cached at the edge for efficient access.

```APIDOC
## GET /models

### Description
Retrieves a list of all available language models with their comprehensive metadata, including architecture, pricing, and supported parameters. The response is cached at the edge and designed for reliable integration with production applications.

### Method
GET

### Endpoint
/models

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
{}

### Response
#### Success Response (200)
- **data** (array of Model objects) - An array containing detailed information for each available language model.

#### Model Object Schema
- **id** (string) - Unique model identifier used in API requests (e.g., "google/gemini-2.5-pro-preview")
- **canonical_slug** (string) - Permanent slug for the model that never changes
- **name** (string) - Human-readable display name for the model
- **created** (number) - Unix timestamp of when the model was added to OpenRouter
- **description** (string) - Detailed description of the model’s capabilities and characteristics
- **context_length** (number) - Maximum context window size in tokens
- **architecture** (Architecture object) - Object describing the model’s technical capabilities
- **pricing** (Pricing object) - Lowest price structure for using this model
- **top_provider** (TopProvider object) - Configuration details for the primary provider
- **per_request_limits** (object | null) - Rate limiting information (null if no limits)
- **supported_parameters** (string[]) - Array of supported API parameters for this model

#### Architecture Object
- **input_modalities** (string[]) - Supported input types: ["file", "image", "text"]
- **output_modalities** (string[]) - Supported output types: ["text"]
- **tokenizer** (string) - Tokenization method used
- **instruct_type** (string | null) - Instruction format type (null if not applicable)

#### Pricing Object
(All pricing values are in USD per token/request/unit. A value of "0" indicates the feature is free.)
- **prompt** (string) - Cost per input token
- **completion** (string) - Cost per output token
- **request** (string) - Fixed cost per API request
- **image** (string) - Cost per image input
- **web_search** (string) - Cost per web search operation
- **internal_reasoning** (string) - Cost for internal reasoning tokens
- **input_cache_read** (string) - Cost per cached input token read
- **input_cache_write** (string) - Cost per cached input token write

#### TopProvider Object
- **context_length** (number) - Provider-specific context limit
- **max_completion_tokens** (number) - Maximum tokens in response
- **is_moderated** (boolean) - Whether content moderation is applied

#### Supported Parameters (details)
- `tools`: Function calling capabilities
- `tool_choice`: Tool selection control
- `max_tokens`: Response length limiting
- `temperature`: Randomness control
- `top_p`: Nucleus sampling
- `reasoning`: Internal reasoning mode
- `include_reasoning`: Include reasoning in response
- `structured_outputs`: JSON schema enforcement
- `response_format`: Output format specification
- `stop`: Custom stop sequences
- `frequency_penalty`: Repetition reduction
- `presence_penalty`: Topic diversity
- `seed`: Deterministic outputs

#### Response Example
```json
{
  "data": [
    {
      "id": "google/gemini-2.5-pro-preview",
      "canonical_slug": "gemini-2.5-pro",
      "name": "Gemini 2.5 Pro",
      "created": 1700000000,
      "description": "A powerful multimodal model from Google.",
      "context_length": 32768,
      "architecture": {
        "input_modalities": ["text", "image"],
        "output_modalities": ["text"],
        "tokenizer": "google-tokenizer",
        "instruct_type": "chat"
      },
      "pricing": {
        "prompt": "0.000001",
        "completion": "0.000002",
        "request": "0",
        "image": "0.000005",
        "web_search": "0",
        "internal_reasoning": "0",
        "input_cache_read": "0",
        "input_cache_write": "0"
      },
      "top_provider": {
        "context_length": 32768,
        "max_completion_tokens": 8192,
        "is_moderated": true
      },
      "per_request_limits": null,
      "supported_parameters": [
        "max_tokens",
        "temperature",
        "top_p",
        "stop"
      ]
    }
  ]
}
```
```

--------------------------------

### POST /api/v1/chat/completions - Cheapest Model with Performance Requirements

Source: https://openrouter.ai/docs/guides/routing/provider-selection

This endpoint allows you to request chat completions, prioritizing the cheapest available model that meets specified performance thresholds like minimum throughput or maximum latency, across a list of potential models.

```APIDOC
## POST /api/v1/chat/completions

### Description
Request chat completions from OpenRouter, with advanced provider selection logic to find the cheapest model that satisfies specific performance requirements (e.g., minimum throughput or maximum latency) from a given list of models.

### Method
POST

### Endpoint
/api/v1/chat/completions

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
- **models** (array of string) - Required - A list of model identifiers (e.g., "anthropic/claude-sonnet-4.5") to consider for the completion.
- **messages** (array of object) - Required - A list of message objects comprising the conversation so far.
  - **messages[].role** (string) - Required - The role of the message sender (e.g., "user", "assistant").
  - **messages[].content** (string) - Required - The content of the message.
- **provider** (object) - Optional - Configuration for advanced provider selection.
  - **provider.sort** (object) - Optional - Sorting criteria for providers.
    - **provider.sort.by** (string) - Optional - The criterion to sort by, e.g., "price".
    - **provider.sort.partition** (string) - Optional - Partitioning strategy, e.g., "none" to consider all models together.
  - **provider.preferred_min_throughput** (object) - Optional - Minimum throughput requirements.
    - **provider.preferred_min_throughput.p90** (number) - Optional - The 90th percentile minimum throughput in tokens/sec that preferred providers should meet.
  - **provider.preferred_max_latency** (object) - Optional - Maximum latency requirements.
    - **provider.preferred_max_latency.p90** (number) - Optional - The 90th percentile maximum latency in seconds that preferred providers should meet.
- **stream** (boolean) - Optional - Whether to stream the response. Defaults to `false`.

### Request Example
```json
{
  "models": [
    "anthropic/claude-sonnet-4.5",
    "openai/gpt-5-mini",
    "google/gemini-3-flash-preview"
  ],
  "messages": [
    {
      "role": "user",
      "content": "Hello"
    }
  ],
  "provider": {
    "sort": {
      "by": "price",
      "partition": "none"
    },
    "preferred_min_throughput": {
      "p90": 50
    },
    "preferred_max_latency": {
      "p90": 3
    }
  },
  "stream": false
}
```

### Response
#### Success Response (200)
- **id** (string) - The unique ID of the completion.
- **object** (string) - The type of object, typically "chat.completion".
- **created** (number) - The Unix timestamp (in seconds) of when the completion was created.
- **model** (string) - The identifier of the model used for the completion.
- **choices** (array of object) - A list of completion choices.
  - **choices[].index** (number) - The index of the choice.
  - **choices[].message** (object) - The message generated by the model.
    - **choices[].message.role** (string) - The role of the message, typically "assistant".
    - **choices[].message.content** (string) - The content of the message.
  - **choices[].finish_reason** (string) - The reason the model stopped generating tokens (e.g., "stop", "length").
- **usage** (object) - Information about the tokens used.
  - **usage.prompt_tokens** (number) - The number of tokens in the prompt.
  - **usage.completion_tokens** (number) - The number of tokens in the completion.
  - **usage.total_tokens** (number) - The total number of tokens used.

#### Response Example
```json
{
  "id": "chatcmpl-abcdef1234567890",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "anthropic/claude-sonnet-4.5",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 12,
    "total_tokens": 22
  }
}
```
```

--------------------------------

### GET /api/v1/guardrails

Source: https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails

List all guardrails for the authenticated user. A management API key is required for this operation.

```APIDOC
## GET /api/v1/guardrails

### Description
List all guardrails for the authenticated user. A management key is required.

### Method
GET

### Endpoint
/api/v1/guardrails

### Parameters
#### Query Parameters
- **offset** (string) - Optional - Number of records to skip for pagination
- **limit** (string) - Optional - Maximum number of records to return (max 100)

#### Headers
- **Authorization** (string) - Required - API key as bearer token in Authorization header

### Request Example
{}

### Response
#### Success Response (200)
- **data** (array of objects) - List of guardrails
  - **id** (string, uuid) - Unique identifier for the guardrail
  - **name** (string) - Name of the guardrail
  - **description** (string, null) - Description of the guardrail
  - **limit_usd** (number, double, null) - Spending limit in USD
  - **reset_interval** (string, enum: daily, weekly, monthly, null) - Interval at which the limit resets (daily, weekly, monthly)
  - **allowed_providers** (array of strings, null) - List of allowed provider IDs
  - **allowed_models** (array of strings, null) - Array of model canonical_slugs (immutable identifiers)
  - **enforce_zdr** (boolean, null) - Whether to enforce zero data retention
  - **created_at** (string) - ISO 8601 timestamp of when the guardrail was created
  - **updated_at** (string, null) - ISO 8601 timestamp of when the guardrail was last updated
- **total_count** (number, double) - Total number of guardrails

#### Response Example
```json
{
  "data": [
    {
      "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
      "name": "My Guardrail",
      "description": "Guardrail for personal projects",
      "limit_usd": 10.50,
      "reset_interval": "monthly",
      "allowed_providers": [
        "openai",
        "anthropic"
      ],
      "allowed_models": [
        "gpt-4",
        "claude-3-opus"
      ],
      "enforce_zdr": true,
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-01T12:00:00Z"
    }
  ],
  "total_count": 1
}
```
```

--------------------------------

### Illustrating OpenRouter `callModel` Message Item Streaming

Source: https://openrouter.ai/docs/sdks/typescript/call-model/working-with-items

This TypeScript example demonstrates how `callModel` streams message items. Each iteration yields a complete item with the same ID but progressively updated content, simplifying state management by replacing the entire item rather than accumulating chunks.

```typescript
// Iteration 1
{
  id: "msg_123",
  type: "message",
  content: [{ type: "output_text", text: "Hello" }]
}

// Iteration 2
{
  id: "msg_123",
  type: "message",
  content: [{ type: "output_text", text: "Hello world" }]
}

// Iteration 3
{
  id: "msg_123",
  type: "message",
  content: [{ type: "output_text", text: "Hello world!" }]
}
```

--------------------------------

### Basic Chat with OpenRouter Model

Source: https://openrouter.ai/docs/guides/community/tanstack-ai

Initialize a basic chat stream using TanStack AI with an OpenRouter model adapter. This example demonstrates the simplest way to send a message and receive a response.

```typescript
import { chat } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

const stream = chat({
  adapter: openRouterText("openai/gpt-5.2"),
  messages: [{ role: "user", content: "Hello!" }],
});
```

--------------------------------

### OpenAPI Specification for Models Count Endpoint

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-count

OpenAPI 3.1.1 specification defining the GET /models/count endpoint. Requires Bearer token authentication in the Authorization header and returns a JSON response containing the total model count. Includes schema definitions for the response structure.

```yaml
openapi: 3.1.1
info:
  title: Get total count of available models
  version: endpoint_models.listModelsCount
paths:
  /models/count:
    get:
      operationId: list-models-count
      summary: Get total count of available models
      tags:
        - - subpackage_models
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the total count of available models
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelsCountResponse'
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    ModelsCountResponseData:
      type: object
      properties:
        count:
          type: number
          format: double
          description: Total number of available models
      required:
        - count
    ModelsCountResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ModelsCountResponseData'
          description: Model count data
      required:
        - data
```

--------------------------------

### GET /api/v1/keys/{hash}

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Retrieves a single API key by its hash identifier. This endpoint requires a valid management key for authentication and returns the details of the specified API key.

```APIDOC
## GET /api/v1/keys/{hash}

### Description
Get a single API key by hash. This endpoint retrieves the details of a specific API key from your OpenRouter account.

### Method
GET

### Endpoint
https://openrouter.ai/api/v1/keys/{hash}

### Parameters
#### Path Parameters
- **hash** (string) - Required - The hash identifier of the API key to retrieve

### Authentication
- **Management Key** - Required - A valid OpenRouter management API key must be provided in the request headers

### Request Example
```
GET https://openrouter.ai/api/v1/keys/abc123def456
Authorization: Bearer YOUR_MANAGEMENT_KEY
```

### Response
#### Success Response (200)
- **hash** (string) - The hash identifier of the API key
- **name** (string) - The name of the API key
- **created_at** (string) - Timestamp when the API key was created
- **last_used_at** (string) - Timestamp of the last usage of this API key
- **is_active** (boolean) - Whether the API key is currently active

#### Response Example
```json
{
  "hash": "abc123def456",
  "name": "My API Key",
  "created_at": "2024-01-15T10:30:00Z",
  "last_used_at": "2024-01-20T14:22:15Z",
  "is_active": true
}
```

#### Error Response (401)
- **error** (string) - Authentication failed or invalid management key provided

#### Error Response (404)
- **error** (string) - API key with the specified hash not found
```

--------------------------------

### Stream Chat Completion Responses and Access Usage Information (OpenRouter API)

Source: https://openrouter.ai/docs/guides/guides/usage-accounting

This example illustrates how to perform streaming chat completions with the OpenRouter API. It highlights how to iterate through streamed chunks, print the content as it arrives, and extract comprehensive usage statistics from the final chunk, including total tokens, prompt tokens, completion tokens, and estimated cost.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="{{API_KEY_REF}}",
)

def chat_completion_streaming(messages):
    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=messages,
        stream=True
    )
    return response

# Usage is always included in the final chunk when streaming
for chunk in chat_completion_streaming([
    {"role": "user", "content": "Write a haiku about Paris."}
]):
    if hasattr(chunk, 'usage') and chunk.usage:
        if hasattr(chunk.usage, 'total_tokens'):
            print(f"\nUsage Statistics:")
            print(f"Total Tokens: {chunk.usage.total_tokens}")
            print(f"Prompt Tokens: {chunk.usage.prompt_tokens}")
            print(f"Completion Tokens: {chunk.usage.completion_tokens}")
            print(f"Cost: {chunk.usage.cost} credits")
    elif chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://openrouter.ai/api/v1',
  apiKey: '{{API_KEY_REF}}',
});

async function chatCompletionStreaming(messages) {
  const response = await openai.chat.completions.create({
    model: '{{MODEL}}',
    messages,
    stream: true,
  });

  return response;
}

// Usage is always included in the final chunk when streaming
(async () => {
  for await (const chunk of chatCompletionStreaming([
    { role: 'user', content: 'Write a haiku about Paris.' },
  ])) {
    if (chunk.usage) {
      console.log('\nUsage Statistics:');
      console.log(`Total Tokens: ${chunk.usage.total_tokens}`);
      console.log(`Prompt Tokens: ${chunk.usage.prompt_tokens}`);
      console.log(`Completion Tokens: ${chunk.usage.completion_tokens}`);
      console.log(`Cost: ${chunk.usage.cost} credits`);
    } else if (chunk.choices[0]?.delta?.content) {
      process.stdout.write(chunk.choices[0].delta.content);
    }
  }
})();
```

--------------------------------

### Delete Guardrail - C# Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/delete-guardrail

C# implementation using RestSharp to send a DELETE request and remove a guardrail.

```APIDOC
### C# Example

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```
```

--------------------------------

### Specify Explicit Provider Order for OpenRouter AI in TypeScript

Source: https://openrouter.ai/docs/guides/community/tanstack-ai

This example demonstrates how to define an explicit order for OpenRouter AI providers to be tried, rather than relying on automatic selection. The `order` array specifies the preferred sequence of providers, and `allow_fallbacks: true` ensures that if a provider in the list fails, the system will attempt the next one.

```typescript
import { chat } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

const stream = chat({
  adapter: openRouterText("anthropic/claude-sonnet-4.5"),
  messages: [{ role: "user", content: "Hello!" }],
  modelOptions: {
    provider: {
      order: ["anthropic", "amazon-bedrock", "google-vertex"],
      allow_fallbacks: true
    }
  }
});
```

--------------------------------

### Delete Guardrail - Java Example

Source: https://openrouter.ai/docs/api/api-reference/guardrails/delete-guardrail

Java implementation using Unirest library to send a DELETE request and remove a guardrail.

```APIDOC
### Java Example

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000")
  .header("Authorization", "Bearer <token>")
  .asString();
```
```

--------------------------------

### Non-Streaming Response Example

Source: https://openrouter.ai/docs/best-practices/reasoning-tokens

Demonstrates how reasoning_details appears in non-streaming API responses. Shows the complete structure with reasoning_details located in the message object containing multiple reasoning detail types.

```APIDOC
## Non-Streaming Response

### Description
In non-streaming responses, `reasoning_details` appears directly in the message object with all reasoning information available immediately.

### Response Structure
```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Based on my analysis, I recommend the following approach...",
        "reasoning_details": [
          {
            "type": "reasoning.summary",
            "summary": "Analyzed the problem by breaking it into components",
            "id": "reasoning-summary-1",
            "format": "anthropic-claude-v1",
            "index": 0
          },
          {
            "type": "reasoning.text",
            "text": "Let me work through this systematically:\n1. First consideration...\n2. Second consideration...",
            "signature": null,
            "id": "reasoning-text-1",
            "format": "anthropic-claude-v1",
            "index": 1
          }
        ]
      }
    }
  ]
}
```
```

--------------------------------

### Fetch Models List - Ruby with Net::HTTP

Source: https://openrouter.ai/docs/api/api-reference/models/get-models

Uses Ruby's built-in Net::HTTP library to make HTTPS GET request to OpenRouter API. Configures SSL connection and sets Authorization header. Returns response body as string.

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

--------------------------------

### List All Providers using OpenRouter Python SDK

Source: https://openrouter.ai/docs/sdks/python/api-reference/providers

This snippet demonstrates how to list all available AI providers using the OpenRouter Python SDK. It initializes the OpenRouter client by retrieving the API key from environment variables and then invokes the `providers.list()` method. The response, containing the list of providers, is subsequently printed to the console.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.providers.list()

    # Handle response
    print(res)
```

--------------------------------

### GET /api/v1/keys/{key_id}

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Retrieves the details of a specific API key identified by its unique ID. This endpoint requires authentication using a bearer token.

```APIDOC
## GET /api/v1/keys/{key_id}

### Description
Retrieves the details of a specific API key identified by its unique ID. This endpoint requires authentication using a bearer token.

### Method
GET

### Endpoint
/api/v1/keys/{key_id}

### Parameters
#### Path Parameters
- **key_id** (string) - Required - The unique identifier of the API key to retrieve.

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
```
GET https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943
Authorization: Bearer <token>
```

### Response
#### Success Response (200)
- **id** (string) - The unique identifier of the API key.
- **created_at** (string) - Timestamp when the key was created (e.g., ISO 8601 format).
- **last_used_at** (string) - Timestamp when the key was last used.
- **name** (string) - The name or description given to the API key.
- **revoked** (boolean) - Indicates if the API key has been revoked.
- **permissions** (array of strings) - List of permissions associated with the key.
- **user_id** (string) - The ID of the user who owns this key.

#### Response Example
```json
{
  "id": "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943",
  "created_at": "2023-01-01T12:00:00Z",
  "last_used_at": "2023-10-26T10:30:00Z",
  "name": "My Application Key",
  "revoked": false,
  "permissions": ["read", "write"],
  "user_id": "user_abc123"
}
```
```

--------------------------------

### Fetch OpenRouter API Keys - Swift

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Uses Foundation's URLSession and NSMutableURLRequest to make an authenticated GET request with custom headers. Includes error handling and HTTP response inspection in the completion handler.

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Fetch OpenRouter API Keys - Java

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Uses the Unirest HTTP client library to make an authenticated GET request to the OpenRouter API. Returns response as a string with Bearer token in the Authorization header.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943")
  .header("Authorization", "Bearer <token>")
  .asString();
```

--------------------------------

### Generate Basic Images using OpenRouter TypeScript SDK

Source: https://openrouter.ai/docs/features/multimodal/image-generation

This TypeScript example demonstrates how to perform basic image generation using the OpenRouter SDK. It sends a chat completion request to the `/api/v1/chat/completions` endpoint, specifying a text prompt and `modalities: ['image', 'text']`. The code then extracts and logs the Base64 data URL of the generated image from the model's response.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '{{API_KEY_REF}}',
});

const result = await openRouter.chat.send({
  model: '{{MODEL}}',
  messages: [
    {
      role: 'user',
      content: 'Generate a beautiful sunset over mountains',
    },
  ],
  modalities: ['image', 'text'],
  stream: false,
});

// The generated image will be in the assistant message
if (result.choices) {
  const message = result.choices[0].message;
  if (message.images) {
    message.images.forEach((image, index) => {
      const imageUrl = image.imageUrl.url; // Base64 data URL
      console.log(`Generated image ${index + 1}: ${imageUrl.substring(0, 50)}...`);
    });
  }
}
```

--------------------------------

### Import and Initialize ListRequest - TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listrequest

Import the ListRequest type from the OpenRouter SDK and create an instance with optional parameters. This example demonstrates basic initialization of a ListRequest object for listing API keys with support for filtering disabled keys and pagination.

```typescript
import { ListRequest } from "@openrouter/sdk/models/operations";

let value: ListRequest = {};
```

--------------------------------

### Enable Fine-Grained Tool Streaming with OpenRouter TypeScript SDK

Source: https://openrouter.ai/docs/features/provider-routing

Demonstrates how to initialize the OpenRouter SDK and send a chat completion request with fine-grained tool streaming enabled via the x-anthropic-beta header. The example shows defining a weather tool and enabling streaming for tool calls on Claude Sonnet 4.5 model.

```TypeScript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
});

const completion = await openRouter.chat.send(
  {
    model: 'anthropic/claude-sonnet-4.5',
    messages: [{ role: 'user', content: 'What is the weather in Tokyo?' }],
    tools: [
      {
        type: 'function',
        function: {
          name: 'get_weather',
          description: 'Get the current weather for a location',
          parameters: {
            type: 'object',
            properties: {
              location: { type: 'string' },
            },
            required: ['location'],
          },
        },
      },
    ],
    stream: true,
  },
  {
    headers: {
      'x-anthropic-beta': 'fine-grained-tool-streaming-2025-05-14',
    },
  },
);
```

--------------------------------

### GET /v1/models

Source: https://openrouter.ai/docs/sdks/python/api-reference/operations/listendpointsresponse

Retrieves a comprehensive list of all available AI models, each detailing its endpoints, pricing, architecture, and performance statistics.

```APIDOC
## GET /v1/models

### Description
Retrieves a comprehensive list of all available AI models, each detailing its endpoints, pricing, architecture, and performance statistics.

### Method
GET

### Endpoint
/v1/models

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(None)

### Response
#### Success Response (200)
- **data** (array of objects) - A list of available AI models. Each object represents a model and contains the following fields:
    - **id** (string) - Unique identifier for the model (e.g., "openai/gpt-4").
    - **name** (string) - Display name of the model (e.g., "GPT-4").
    - **created** (number) - Unix timestamp of when the model was created.
    - **description** (string) - A brief description of the model's capabilities.
    - **architecture** (object) - Details about the model's architecture.
        - **tokenizer** (string) - The tokenizer used by the model (e.g., "GPT").
        - **instruct_type** (string) - Instruction type (e.g., "chatml").
        - **modality** (string) - Primary modality (e.g., "text->text").
        - **input_modalities** (array of strings) - Supported input modalities (e.g., ["text"]).
        - **output_modalities** (array of strings) - Supported output modalities (e.g., ["text"]).
    - **endpoints** (array of objects) - A list of specific endpoints available for this model. Each endpoint object contains:
        - **name** (string) - Name of the endpoint (e.g., "OpenAI: GPT-4").
        - **model_name** (string) - The model name associated with this endpoint (e.g., "GPT-4").
        - **context_length** (number) - Maximum context length in tokens.
        - **pricing** (object) - Pricing details for the endpoint.
            - **prompt** (string) - Cost per prompt token (e.g., "0.00003").
            - **completion** (string) - Cost per completion token (e.g., "0.00006").
            - **request** (string) - Cost per request (e.g., "0").
            - **image** (string) - Cost per image (e.g., "0").
        - **provider_name** (string) - Name of the provider (e.g., "OpenAI").
        - **tag** (string) - Provider tag (e.g., "openai").
        - **quantization** (string) - Quantization level (e.g., "fp16").
        - **max_completion_tokens** (number) - Maximum tokens for completion.
        - **max_prompt_tokens** (number) - Maximum tokens for prompt.
        - **supported_parameters** (array of strings) - List of supported API parameters (e.g., "temperature", "top_p").
        - **status** (string) - Current status of the endpoint (e.g., "default").
        - **uptime_last_30m** (number) - Uptime percentage over the last 30 minutes.
        - **supports_implicit_caching** (boolean) - Indicates if implicit caching is supported.
        - **latency_last_30m** (object) - Latency statistics over the last 30 minutes.
            - **p50** (number) - 50th percentile latency.
            - **p75** (number) - 75th percentile latency.
            - **p90** (number) - 90th percentile latency.
            - **p99** (number) - 99th percentile latency.
        - **throughput_last_30m** (object) - Throughput statistics over the last 30 minutes.
            - **p50** (number) - 50th percentile throughput.
            - **p75** (number) - 75th percentile throughput.
            - **p90** (number) - 90th percentile throughput.
            - **p99** (number) - 99th percentile throughput.

#### Response Example
```json
[
  {
    "id": "openai/gpt-4",
    "name": "GPT-4",
    "created": 1692901234,
    "description": "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy.",
    "architecture": {
      "tokenizer": "GPT",
      "instruct
```

--------------------------------

### Retrieve API Key Information - PHP

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key

Uses Guzzle HTTP client to make an authenticated GET request. Requires Guzzle dependency via Composer. Returns response body containing API key information.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/key', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

--------------------------------

### GET /guardrails/{id}

Source: https://openrouter.ai/docs/sdks/python/api-reference/guardrails

Retrieves a single guardrail's details by its unique identifier. A provisioning key is required for authentication.

```APIDOC
## GET /guardrails/{id}

### Description
Retrieves a single guardrail's details by its unique identifier. A provisioning key is required for authentication.

### Method
GET

### Endpoint
/guardrails/{id}

### Parameters
#### Path Parameters
- **id** (string) - Required - The unique identifier of the guardrail.

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(None)

### Response
#### Success Response (200)
- **id** (string) - The unique identifier of the guardrail.
- **name** (string) - Name of the guardrail.
- **description** (string, nullable) - Description of the guardrail.
- **limit_usd** (float, nullable) - Spending limit in USD.
- **reset_interval** (string, nullable) - Interval at which the limit resets (daily, weekly, monthly).
- **allowed_providers** (array of strings) - List of allowed provider IDs.
- **allowed_models** (array of strings) - Array of model identifiers.
- **enforce_zdr** (boolean, nullable) - Whether zero data retention is enforced.
- **created_at** (string) - Timestamp of guardrail creation.

#### Response Example
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Example Guardrail",
  "description": "Limits usage for a specific project",
  "limit_usd": 100.0,
  "reset_interval": "monthly",
  "allowed_providers": [
    "openai",
    "anthropic"
  ],
  "allowed_models": [
    "openai/gpt-4",
    "anthropic/claude-3-opus"
  ],
  "enforce_zdr": true,
  "created_at": "2023-10-26T14:30:00Z"
}
```

### Errors
- **errors.BadRequestResponseError** (400) - application/json
- **errors.UnauthorizedResponseError** (401) - application/json
- **errors.InternalServerResponseError** (500) - application/json
- **errors.OpenRouterDefaultError** (4XX, 5XX) - */*
```

--------------------------------

### List API Keys - Ruby

Source: https://openrouter.ai/docs/api/api-reference/api-keys/list

Retrieve API keys using Ruby's Net::HTTP library. Establishes an HTTPS connection to the OpenRouter API and sends an authenticated GET request. Returns the response body containing API keys.

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

--------------------------------

### Enable Interleaved Thinking with Python Requests

Source: https://openrouter.ai/docs/guides/routing/provider-selection

Shows how to enable interleaved thinking using Python's requests library for step-by-step problem solving through OpenRouter API. Includes proper header configuration with beta feature flag for reasoning tasks. Requires Bearer token authentication and requests library.

```python
import requests

headers = {
  'Authorization': 'Bearer <OPENROUTER_API_KEY>',
  'Content-Type': 'application/json',
  'x-anthropic-beta': 'interleaved-thinking-2025-05-14',
}

response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
  'model': 'anthropic/claude-sonnet-4.5',
  'messages': [{ 'role': 'user', 'content': 'Solve this step by step: What is 15% of 240?' }],
  'stream': True,
})
```

--------------------------------

### GET /api/v1/key

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key

Retrieves information on the API key associated with the current authentication session. This endpoint requires valid authentication credentials and returns details about the active API key.

```APIDOC
## GET /api/v1/key

### Description
Get information on the API key associated with the current authentication session.

### Method
GET

### Endpoint
https://openrouter.ai/api/v1/key

### Parameters
No parameters required.

### Authentication
This endpoint requires valid API key authentication in the request headers.

### Request Example
```
GET /api/v1/key HTTP/1.1
Host: openrouter.ai
Authorization: Bearer YOUR_API_KEY
```

### Response
#### Success Response (200)
- **key** (string) - The API key value
- **created_at** (string) - Timestamp when the key was created
- **last_used_at** (string) - Timestamp of last usage
- **name** (string) - Name or identifier for the key
- **usage** (object) - Usage statistics for the key

#### Response Example
```json
{
  "key": "sk-or-v1-xxxxxxxxxxxxx",
  "created_at": "2024-01-15T10:30:00Z",
  "last_used_at": "2024-01-20T14:45:30Z",
  "name": "Production Key",
  "usage": {
    "requests": 1250,
    "tokens": 45000
  }
}
```

### Error Responses
#### 401 Unauthorized
Invalid or missing authentication credentials.

#### 404 Not Found
API key not found for the current session.

### Reference
https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key
```

--------------------------------

### Examine OpenRouter API Streaming Output (Server-Sent Events)

Source: https://openrouter.ai/docs/api/reference/responses/basic-usage

This snippet provides an example of the raw Server-Sent Events (SSE) data received when streaming is enabled from the OpenRouter API. It illustrates the various event types like 'response.created', 'response.output_item.added', 'response.content_part.delta', and 'response.done', showing how content is delivered incrementally.

```text
data: {"type":"response.created","response":{"id":"resp_1234567890","object":"response","status":"in_progress"}}

data: {"type":"response.output_item.added","response_id":"resp_1234567890","output_index":0,"item":{"type":"message","id":"msg_abc123","role":"assistant","status":"in_progress","content":[]}}

data: {"type":"response.content_part.added","response_id":"resp_1234567890","output_index":0,"content_index":0,"part":{"type":"output_text","text":""}}

data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":"Once"}

data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":" upon"}

data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":" a"}

data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":" time"}

data: {"type":"response.output_item.done","response_id":"resp_1234567890","output_index":0,"item":{"type":"message","id":"msg_abc123","role":"assistant","status":"completed","content":[{"type":"output_text","text":"Once upon a time, in a world where artificial intelligence had become as common as smartphones..."}]}}

data: {"type":"response.done","response":{"id":"resp_1234567890","object":"response","status":"completed","usage":{"input_tokens":12,"output_tokens":45,"total_tokens":57}}}

data: [DONE]
```

--------------------------------

### GET /api/v1/models/user

Source: https://openrouter.ai/docs/api/api-reference/models/list-models-user

Retrieves a list of AI models that are available to the authenticated user. This endpoint provides details such as model pricing, context length, architecture, and supported parameters for each model.

```APIDOC
## GET /api/v1/models/user

### Description
Retrieves a list of AI models that are available to the authenticated user. This endpoint provides details such as model pricing, context length, architecture, and supported parameters for each model.

### Method
GET

### Endpoint
/api/v1/models/user

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(Not applicable for GET request without body)

### Response
#### Success Response (200)
- **data** (array of Model objects) - A list of models available to the user, each containing properties like pricing, context_length, architecture, etc.

#### Response Example
```json
{
  "data": [
    {
      "pricing": {
        "prompt": "0.001",
        "completion": "0.002"
      },
      "context_length": 4096,
      "architecture": "Transformer",
      "top_provider": true,
      "per_request_limits": {
        "max_tokens": 2048
      },
      "supported_parameters": [
        "temperature",
        "top_p"
      ],
      "default_parameters": {
        "temperature": 0.7
      }
    },
    {
      "pricing": {
        "prompt": "0.005",
        "completion": "0.006"
      },
      "context_length": 8192,
      "architecture": "RNN",
      "top_provider": false,
      "per_request_limits": {
        "max_tokens": 4096
      },
      "supported_parameters": [
        "temperature"
      ],
      "default_parameters": {
        "temperature": 0.8
      }
    }
  ]
}
```
```

--------------------------------

### GET /api/v1/embeddings/models

Source: https://openrouter.ai/docs/api/api-reference/embeddings/list-embeddings-models

This endpoint retrieves a list of all available embedding models supported by OpenRouter. It requires authentication via a Bearer token in the 'Authorization' header.

```APIDOC
## GET /api/v1/embeddings/models

### Description
This endpoint retrieves a list of all available embedding models supported by OpenRouter. It requires authentication via a Bearer token in the 'Authorization' header.

### Method
GET

### Endpoint
/api/v1/embeddings/models

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
{}

### Response
#### Success Response (200)
- **data** (array of objects) - A list of available embedding models.
  - **id** (string) - Unique identifier for the model.
  - **name** (string) - Human-readable name of the model.
  - **dimensions** (integer) - The dimensionality of the embeddings produced by the model.
- **object** (string) - The type of object returned, typically "list".

#### Response Example
{
  "data": [
    {
      "id": "embed-model-1",
      "name": "Embedding Model One",
      "dimensions": 1536
    },
    {
      "id": "embed-model-2",
      "name": "Embedding Model Two",
      "dimensions": 768
    }
  ],
  "object": "list"
}
```

--------------------------------

### Handle Missing Skills with Graceful Fallback

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

Provides error handling for missing skill files by checking existence before processing. Returns a helpful message listing available skills when a requested skill cannot be found.

```typescript
execute: async (params) => {
  if (!existsSync(skillPath)) {
    return `Skill not found. Available: ${listAvailableSkills().join(', ')}`;
  }
  // ...
};
```

--------------------------------

### List API Keys - Java

Source: https://openrouter.ai/docs/api/api-reference/api-keys/list

Retrieve API keys using Java's Unirest HTTP client library. Sends an authenticated GET request with Bearer token header. Returns response as a string containing the API keys data.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/keys")
  .header("Authorization", "Bearer <token>")
  .asString();
```

--------------------------------

### GET /guardrails/assignments/keys

Source: https://openrouter.ai/docs/sdks/python/api-reference/guardrails

List all API key guardrail assignments for the authenticated user. Supports pagination with offset and limit parameters. Requires provisioning key authentication.

```APIDOC
## GET /guardrails/assignments/keys

### Description
List all API key guardrail assignments for the authenticated user. Provisioning key required.

### Method
GET

### Endpoint
/guardrails/assignments/keys

### Parameters
#### Query Parameters
- **offset** (string) - Optional - Number of records to skip for pagination. Example: 0
- **limit** (string) - Optional - Maximum number of records to return (max 100). Example: 50
- **retries** (Optional[utils.RetryConfig]) - Optional - Configuration to override the default retry behavior of the client

### Request Example
```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:
    res = open_router.guardrails.list_key_assignments()
    print(res)
```

### Response
#### Success Response (200)
- **operations.ListKeyAssignmentsResponse** - List of API key guardrail assignments

### Errors
| Error Type | Status Code | Content Type |
|---|---|---|
| UnauthorizedResponseError | 401 | application/json |
| InternalServerResponseError | 500 | application/json |
| OpenRouterDefaultError | 4XX, 5XX | */* |
```

--------------------------------

### Define PerRequestLimits object in TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/perrequestlimits

This example demonstrates how to import and instantiate a `PerRequestLimits` object in TypeScript. It shows how to set the maximum `promptTokens` and `completionTokens` for a single request, which are crucial for managing API usage.

```typescript
import { PerRequestLimits } from "@openrouter/sdk/models";

let value: PerRequestLimits = {
  promptTokens: 1000,
  completionTokens: 1000,
};
```

--------------------------------

### Initialize ProviderPreferences object in TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/providerpreferences

This example demonstrates how to import and initialize an empty `ProviderPreferences` object using the OpenRouter TypeScript SDK. It shows the basic structure for setting up provider routing preferences.

```typescript
import { ProviderPreferences } from "@openrouter/sdk/models";

let value: ProviderPreferences = {};
```

--------------------------------

### List Guardrail Key Assignments (Python)

Source: https://openrouter.ai/docs/sdks/python/api-reference/guardrails

This Python example demonstrates how to retrieve all API key assignments for a specific guardrail using the OpenRouter SDK. It initializes the client with an API key from environment variables and then calls the `list_guardrail_key_assignments` method, passing the guardrail's unique identifier. The response, containing the list of assignments, is then printed.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.list_guardrail_key_assignments(id="550e8400-e29b-41d4-a716-446655440000")

    # Handle response
    print(res)
```

--------------------------------

### Adjust Temperature Adaptively in OpenRouter SDK

Source: https://openrouter.ai/docs/sdks/typescript/call-model/dynamic-parameters

This example illustrates how to dynamically adjust the `temperature` parameter based on the conversation context. By analyzing the last message in `ctx.turnRequest`, the model's creativity can be increased for creative tasks or reduced for precise tasks like coding or calculations.

```typescript
const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  temperature: (ctx) => {
    // Analyze recent messages for task type
    const lastMessage = JSON.stringify(ctx.turnRequest?.input).toLowerCase();

    if (lastMessage.includes('creative') || lastMessage.includes('brainstorm')) {
      return 1.0; // Creative tasks
    }
    if (lastMessage.includes('code') || lastMessage.includes('calculate')) {
      return 0.2; // Precise tasks
    }
    return 0.7; // Default
  },
  input: 'Write a creative story',
});
```

--------------------------------

### Instantiate DeleteKeysResponse in TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/deletekeysresponse

This example demonstrates how to create an instance of the `DeleteKeysResponse` object in TypeScript, confirming that an API key was successfully deleted. It shows the basic structure for initializing the response object with the `deleted` property set to `true`.

```typescript
import { DeleteKeysResponse } from "@openrouter/sdk/models/operations";

let value: DeleteKeysResponse = {
  deleted: true,
};
```

--------------------------------

### Specify a Single Model for Text Generation (TypeScript)

Source: https://openrouter.ai/docs/sdks/call-model/text-generation

This example demonstrates how to explicitly select a single model for text generation by providing its OpenRouter ID to the `model` parameter in `callModel`.

```typescript
const result = openrouter.callModel({
  model: 'anthropic/claude-sonnet-4.5',
  input: 'Hello!',
});
```

--------------------------------

### List API Keys - C#

Source: https://openrouter.ai/docs/api/api-reference/api-keys/list

Retrieve API keys using C#'s RestSharp library. Creates a REST client and executes an authenticated GET request with Bearer token authorization. Returns the HTTP response containing API keys.

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/keys");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

--------------------------------

### Enable Fine-Grained Tool Streaming with Fetch API

Source: https://openrouter.ai/docs/guides/routing/provider-selection

Shows how to make a direct HTTP POST request to OpenRouter API endpoint with fine-grained tool streaming enabled using the Fetch API. Includes proper headers for authentication and beta feature activation, with a tool definition for weather queries. Requires Bearer token authentication.

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer <OPENROUTER_API_KEY>',
    'Content-Type': 'application/json',
    'x-anthropic-beta': 'fine-grained-tool-streaming-2025-05-14',
  },
  body: JSON.stringify({
    model: 'anthropic/claude-sonnet-4.5',
    messages: [{ role: 'user', content: 'What is the weather in Tokyo?' }],
    tools: [
      {
        type: 'function',
        function: {
          name: 'get_weather',
          description: 'Get the current weather for a location',
          parameters: {
            type: 'object',
            properties: {
              location: { type: 'string' },
            },
            required: ['location'],
          },
        },
      },
    ],
    stream: true,
  }),
});
```

--------------------------------

### GET /providers

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/providers

List all providers available through OpenRouter. This endpoint retrieves a comprehensive list of all provider information that can be used with the OpenRouter API.

```APIDOC
## GET /providers

### Description
List all providers available through OpenRouter. Returns information about all supported providers.

### Method
GET

### Endpoint
/providers

### Parameters
#### Request Options
- **options** (RequestOptions) - Optional - Used to set various options for making HTTP requests
- **options.fetchOptions** (RequestInit) - Optional - Options passed to the underlying HTTP request. Supports all Request options except method and body
- **options.retries** (RetryConfig) - Optional - Enables retrying HTTP requests under certain failure conditions

### Request Example
```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.providers.list();
  console.log(result);
}

run();
```

### Standalone Function Example
```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { providersList } from "@openrouter/sdk/funcs/providersList.js";

const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await providersList(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("providersList failed:", res.error);
  }
}

run();
```

### Response
#### Success Response (200)
- **Promise<operations.ListProvidersResponse>** - List of all available providers with their information

### Error Handling
#### Error Responses
- **500** (InternalServerResponseError) - application/json - Internal server error
- **4XX, 5XX** (OpenRouterDefaultError) - */* - Default error response for client and server errors
```

--------------------------------

### GET /guardrails/assignments/keys

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/guardrails

This endpoint allows authenticated users to retrieve a list of all API key guardrail assignments. A provisioning key is required for access.

```APIDOC
## GET /guardrails/assignments/keys

### Description
List all API key guardrail assignments for the authenticated user. Provisioning key required.

### Method
GET

### Endpoint
/guardrails/assignments/keys

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(No request body for GET requests)

### Response
#### Success Response (200)
- **assignments** (array of objects) - A list of API key guardrail assignments. Each object represents an assignment.

#### Response Example
```json
[
  {
    "id": "string",
    "key_id": "string",
    "guardrail_id": "string",
    "created_at": "datetime"
  }
]
```

### Errors
- **401 UnauthorizedResponseError**: The request is not authenticated.
- **404 NotFoundResponseError**: The requested resource was not found.
- **500 InternalServerResponseError**: An unexpected error occurred on the server.
- **4XX, 5XX OpenRouterDefaultError**: Generic error for various client or server issues.
```

--------------------------------

### API Authentication Guide

Source: https://openrouter.ai/docs/api/authentication

This section details how to authenticate requests to the OpenRouter API using an API key, either directly via HTTP headers or through the OpenAI SDK.

```APIDOC
## Authentication Guide

### Description
This guide explains how to authenticate your requests when interacting with the OpenRouter API. OpenRouter uses Bearer tokens for authentication, allowing direct `curl` usage or integration with OpenAI SDKs. API keys are more powerful than direct model API keys, supporting credit limits and OAuth flows.

### Method
N/A (Authentication Mechanism)

### Endpoint
N/A (Applies to all authenticated endpoints)

### Parameters
#### Request Headers
- **Authorization** (string) - Required - Your OpenRouter API key prefixed with `Bearer `. Example: `Bearer sk-YOUR_API_KEY`
- **HTTP-Referer** (string) - Optional - Your site URL for rankings on openrouter.ai.
- **X-Title** (string) - Optional - Your site title for rankings on openrouter.ai.

### Request Example
```
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer sk-YOUR_API_KEY" \
  -H "HTTP-Referer: YOUR_SITE_URL" \
  -H "X-Title: YOUR_SITE_NAME" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-5.2",
    "messages": [{"role": "user", "content": "Say this is a test"}]
  }'
```

### Response
#### Success Response (200)
(Authentication is implicit in successful API calls; no specific authentication response. A successful response from an authenticated endpoint indicates successful authentication.)

#### Response Example
```json
{
  "id": "chatcmpl-...",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "openai/gpt-5.2",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "This is a test."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 4,
    "completion_tokens": 4,
    "total_tokens": 8
  }
}
```
```

--------------------------------

### GET /user/activity - GetUserActivityResponse

Source: https://openrouter.ai/docs/sdks/python/api-reference/operations/getuseractivityresponse

Retrieves user activity data grouped by endpoint. Returns a structured response containing a list of activity items that track user interactions with the OpenRouter API.

```APIDOC
## GET /user/activity

### Description
Returns user activity data grouped by endpoint. This endpoint provides detailed information about user interactions with various API endpoints.

### Method
GET

### Endpoint
/user/activity

### Response
#### Success Response (200)
- **data** (List[ActivityItem]) - Required - List of activity items containing user interaction data grouped by endpoint

#### Response Schema
```
{
  "data": [
    {
      "endpoint": "string",
      "timestamp": "string",
      "method": "string",
      "status": "integer",
      "duration_ms": "number"
    }
  ]
}
```

### Response Fields
| Field | Type | Description |
|-------|------|-------------|
| `data` | List[ActivityItem] | List of activity items representing user interactions with API endpoints |

### Notes
- The Python SDK and documentation are currently in beta
- Activity items are grouped by endpoint for easier analysis
- For issues or bug reports, visit the [GitHub repository](https://github.com/OpenRouterTeam/python-sdk/issues)
```

--------------------------------

### Handle Streaming with Usage Information in Python

Source: https://openrouter.ai/docs/use-cases/usage-accounting

This example demonstrates how to stream responses from the OpenRouter API using the OpenAI Python client, specifically focusing on extracting usage information from the final chunk of the stream. It initializes the client, defines a streaming chat completion function, and then iterates through the chunks to print content and usage statistics.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="{{API_KEY_REF}}"
)

def chat_completion_streaming(messages):
    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=messages,
        stream=True
    )
    return response

# Usage is always included in the final chunk when streaming
for chunk in chat_completion_streaming([
    {"role": "user", "content": "Write a haiku about Paris."}
]):
    if hasattr(chunk, 'usage') and chunk.usage:
        if hasattr(chunk.usage, 'total_tokens'):
            print(f"\nUsage Statistics:")
            print(f"Total Tokens: {chunk.usage.total_tokens}")
            print(f"Prompt Tokens: {chunk.usage.prompt_tokens}")
            print(f"Completion Tokens: {chunk.usage.completion_tokens}")
            print(f"Cost: {chunk.usage.cost} credits")
    elif chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

--------------------------------

### List all OpenRouter models using `modelsList` standalone function (TypeScript)

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/models

This TypeScript example demonstrates how to fetch a list of all available models from OpenRouter using the `modelsList` standalone function. It initializes `OpenRouterCore` with an API key from environment variables and logs the result or any encountered errors.

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { modelsList } from "@openrouter/sdk/funcs/modelsList.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await modelsList(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("modelsList failed:", res.error);
  }
}

run();
```

--------------------------------

### Get Specific OpenRouter API Key

Source: https://openrouter.ai/docs/guides/overview/auth/management-api-keys

Shows how to retrieve the details of a specific OpenRouter API key using its unique hash. A Management API key is required for authorization.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: 'your-management-key', // Use your Management API key
});

// Get a specific key
const keyHash = '<YOUR_KEY_HASH>';
const key = await openRouter.apiKeys.get(keyHash);
```

```python
import requests

MANAGEMENT_API_KEY = "your-management-key"
BASE_URL = "https://openrouter.ai/api/v1/keys"

# Get a specific key
key_hash = "<YOUR_KEY_HASH>"
response = requests.get(
    f"{BASE_URL}/{key_hash}",
    headers={
        "Authorization": f"Bearer {MANAGEMENT_API_KEY}",
        "Content-Type": "application/json"
    }
)
```

```typescript
const MANAGEMENT_API_KEY = 'your-management-key';
const BASE_URL = 'https://openrouter.ai/api/v1/keys';

// Get a specific key
const keyHash = '<YOUR_KEY_HASH>';
const getKey = await fetch(`${BASE_URL}/${keyHash}`, {
  headers: {
    Authorization: `Bearer ${MANAGEMENT_API_KEY}`,
    'Content-Type': 'application/json',
  },
});
```

--------------------------------

### Configure Image Aspect Ratio and Size with OpenRouter Python API

Source: https://openrouter.ai/docs/features/multimodal/image-generation

This Python example demonstrates how to customize image generation by setting specific `aspect_ratio` and `image_size` parameters within the `image_config` object in an OpenRouter chat completions API request. It shows how to send a request to generate an image with desired dimensions (e.g., 16:9 aspect ratio, 4K resolution) and then process the resulting image URL from the API response.

```python
import requests
import json

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY_REF}",
    "Content-Type": "application/json"
}

payload = {
    "model": "{{MODEL}}",
    "messages": [
        {
            "role": "user",
            "content": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
        }
    ],
    "modalities": ["image", "text"],
    "image_config": {
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()

if result.get("choices"):
    message = result["choices"][0]["message"]
    if message.get("images"):
        for image in message["images"]:
            image_url = image["image_url"]["url"]
            print(f"Generated image: {image_url[:50]}...")
```

--------------------------------

### Instantiate BulkUnassignKeysFromGuardrailResponse in TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/bulkunassignkeysfromguardrailresponse

This example demonstrates how to create an instance of the `BulkUnassignKeysFromGuardrailResponse` object in TypeScript. It shows the basic structure for representing the result of a bulk unassignment operation, specifically setting the `unassignedCount` property.

```typescript
import { BulkUnassignKeysFromGuardrailResponse } from "@openrouter/sdk/models/operations";

let value: BulkUnassignKeysFromGuardrailResponse = {
  unassignedCount: 3,
};
```

--------------------------------

### OpenAIResponsesPrompt Model Definition

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/openairesponsesprompt

Defines the structure of the OpenAIResponsesPrompt object used in the OpenRouter TypeScript SDK, including its fields and an example of its usage.

```APIDOC
## Model: OpenAIResponsesPrompt

### Description
This model defines the structure for an OpenAIResponsesPrompt object within the OpenRouter TypeScript SDK. It specifies the properties and their types for representing a prompt response.

### Fields
- **id** (string) - Required - Unique identifier for the prompt response.
- **variables** (Record<string, models.Variables>) - Optional - A dictionary of variables associated with the prompt response.

### Example Usage (TypeScript)
```typescript
import { OpenAIResponsesPrompt } from "@openrouter/sdk/models";

let value: OpenAIResponsesPrompt = {
  id: "<id>",
};
```
```

--------------------------------

### Fetch Models List - Swift with URLSession

Source: https://openrouter.ai/docs/api/api-reference/models/get-models

Uses Swift's URLSession framework to make HTTPS GET request with custom headers. Includes error handling in completion handler. Demonstrates asynchronous data task execution with resume().

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Access Tool Execution Metadata with getResponse() in JavaScript

Source: https://openrouter.ai/docs/sdks/call-model/tools

This JavaScript example demonstrates how to retrieve comprehensive execution metadata, including the final output and usage statistics, after a model call involving tools. The `getResponse()` method provides access to the `response` object, which contains details about all execution rounds.

```javascript
const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  input: 'What is 2+2 and the weather in Paris?',
  tools: [calculatorTool, weatherTool],
});

const response = await result.getResponse();

// Response includes all execution rounds
console.log('Final output:', response.output);
console.log('Usage:', response.usage);
```

--------------------------------

### Load Multiple AI Skills with TypeScript Tool

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

This TypeScript tool facilitates loading multiple AI skills in a single call for complex tasks. It defines input and output schemas for skill names, dynamically injects skill content into the model's context, and handles checking for skill existence and content retrieval from a specified directory.

```typescript
const multiSkillLoader = tool({
  name: 'load_skills',
  description: 'Load multiple skills at once for complex tasks',

  inputSchema: z.object({
    skills: z.array(z.string()).describe('Array of skill names to load'),
  }),

  outputSchema: z.object({
    loaded: z.array(z.string()),
    failed: z.array(
      z.object({
        name: z.string(),
        reason: z.string(),
      })
    ),
  }),

  nextTurnParams: {
    input: (params, context) => {
      let newInput = Array.isArray(context.input) ? context.input : [context.input];

      for (const skillName of params.skills) {
        const skillMarker = `[Skill: ${skillName}]`;

        // Skip if already loaded
        if (JSON.stringify(newInput).includes(skillMarker)) {
          continue;
        }

        const skillPath = path.join(SKILLS_DIR, skillName, 'SKILL.md');
        if (!existsSync(skillPath)) {
          continue;
        }

        const skillContent = readFileSync(skillPath, 'utf-8');
        const skillDir = path.join(SKILLS_DIR, skillName);

        newInput = [
          ...newInput,
          {
            role: 'user',
            content: `${skillMarker}
Base directory: ${skillDir}

${skillContent}`,
          },
        ];
      }

      return newInput;
    },
  },

  execute: async ({ skills }) => {
    const loaded: string[] = [];
    const failed: Array<{ name: string; reason: string }> = [];

    for (const skill of skills) {
      const skillPath = path.join(SKILLS_DIR, skill, 'SKILL.md');
      if (existsSync(skillPath)) {
        loaded.push(skill);
      } else {
        failed.push({ name: skill, reason: 'Skill not found' });
      }
    }

    return { loaded, failed };
  },
});

// Usage
const result = openrouter.callModel({
  model: 'anthropic/claude-sonnet-4.5',
  input: 'I need to analyze a PDF report and create visualizations',
  tools: [multiSkillLoader],
});
// Model might call: load_skills({ skills: ['pdf-processing', 'data-analysis'] })
```

--------------------------------

### Send chat completion with provider fallback order

Source: https://openrouter.ai/docs/guides/routing/provider-selection

Configure OpenRouter to attempt chat completions with a specified provider order, falling back to default providers if the primary choices fail. This example uses the Mixtral model and specifies OpenAI and Together as preferred providers in order.

```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
});

const completion = await openRouter.chat.send({
  model: 'mistralai/mixtral-8x7b-instruct',
  messages: [{ role: 'user', content: 'Hello' }],
  provider: {
    order: ['openai', 'together'],
  },
  stream: false,
});
```

```typescript
fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer <OPENROUTER_API_KEY>',
    'HTTP-Referer': '<YOUR_SITE_URL>',
    'X-Title': '<YOUR_SITE_NAME>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'mistralai/mixtral-8x7b-instruct',
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      order: ['openai', 'together'],
    },
  }),
});
```

```python
import requests

headers = {
  'Authorization': 'Bearer <OPENROUTER_API_KEY>',
  'HTTP-Referer': '<YOUR_SITE_URL>',
  'X-Title': '<YOUR_SITE_NAME>',
  'Content-Type': 'application/json',
}

response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
  'model': 'mistralai/mixtral-8x7b-instruct',
  'messages': [{ 'role': 'user', 'content': 'Hello' }],
  'provider': {
    'order': ['openai', 'together'],
  },
})
```

--------------------------------

### Import and Initialize ListGuardrailsRequest - TypeScript

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listguardrailsrequest

Demonstrates how to import the ListGuardrailsRequest type from the OpenRouter SDK and create an instance. This is the basic setup required to use the guardrails listing functionality with optional pagination parameters.

```typescript
import { ListGuardrailsRequest } from "@openrouter/sdk/models/operations";

let value: ListGuardrailsRequest = {};
```

--------------------------------

### GET /endpoints

Source: https://openrouter.ai/docs/sdks/python/api-reference/operations/listendpointszdrresponse

This endpoint retrieves a list of all available public endpoints. It provides comprehensive details for each endpoint, including its identifier, name, associated provider, URL, and pricing structure.

```APIDOC
## GET /endpoints\n\n### Description\nReturns a list of all available public endpoints, including details like ID, name, provider, URL, description, and pricing information.\n\n### Method\nGET\n\n### Endpoint\n/endpoints\n\n### Parameters\n#### Path Parameters\n(None)\n\n#### Query Parameters\n(None)\n\n#### Request Body\n(None)\n\n### Request Example\n(Not applicable for this GET request)\n\n### Response\n#### Success Response (200)\n- **data** (List[object]) - A list of public endpoint objects. Each object contains details such as `id`, `name`, `provider`, `url`, `description`, and `pricing` information.\n\n#### Response Example\n```json\n{\n  "data": [\n    {\n      "id": "model-id-1",\n      "name": "Model Name 1",\n      "provider": "Provider A",\n      "url": "https://api.openrouter.ai/v1/models/model-id-1",\n      "description": "A description of the model",\n      "pricing": {\n        "prompt_token_cost": 0.00001,\n        "completion_token_cost": 0.00002\n      }\n    },\n    {\n      "id": "model-id-2",\n      "name": "Model Name 2",\n      "provider": "Provider B",\n      "url": "https://api.openrouter.ai/v1/models/model-id-2",\n      "description": "Another model description",\n      "pricing": {\n        "prompt_token_cost": 0.000015,\n        "completion_token_cost": 0.000025\n      }\n    }\n  ]\n}\n```
```

--------------------------------

### Filter OpenRouter Traces by Model with TraceQL

Source: https://openrouter.ai/docs/guides/features/broadcast/grafana

TraceQL query to filter OpenRouter traces by a specific AI model. This example filters for GPT-4 Turbo requests, combining service name and model attributes for targeted trace retrieval.

```traceql
{ resource.service.name = "openrouter" && span.gen_ai.request.model = "openai/gpt-4-turbo" }
```

--------------------------------

### Fetch OpenRouter API Keys - JavaScript

Source: https://openrouter.ai/docs/api/api-reference/api-keys/get-key

Uses the Fetch API to make an authenticated GET request with async/await pattern and error handling. Returns parsed JSON response from the OpenRouter API keys endpoint.

```javascript
const url = 'https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

--------------------------------

### Preserve Context by Appending to Input Array

Source: https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader

Maintains existing input context by converting it to an array format and appending new messages instead of replacing. Ensures all previous context is retained across multiple tool turns.

```typescript
nextTurnParams: {
  input: (params, context) => {
    const currentInput = Array.isArray(context.input)
      ? context.input
      : [context.input];
    return [...currentInput, newMessage]; // Append, don't replace
  },
};
```

--------------------------------

### GET /models

Source: https://openrouter.ai/docs/sdks/python/api-reference/models/models

List all models and their properties available through the OpenRouter API. Supports filtering by category and supported parameters to help you find the right model for your use case.

```APIDOC
## GET /models

### Description
List all models and their properties

### Method
GET

### Endpoint
/models

### Parameters
#### Query Parameters
- **category** (Optional[operations.Category]) - Optional - Filter models by use case category (e.g., programming)
- **supported_parameters** (Optional[str]) - Optional - Filter by supported parameters
- **retries** (Optional[utils.RetryConfig]) - Optional - Configuration to override the default retry behavior of the client.

### Request Example
```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:
    res = open_router.models.list(category="programming")
    print(res)
```

### Response
#### Success Response (200)
- **ModelsListResponse** (components.ModelsListResponse) - Response containing list of all available models and their properties

### Error Handling
| Error Type | Status Code | Content Type |
| --- | --- | --- |
| BadRequestResponseError | 400 | application/json |
| InternalServerResponseError | 500 | application/json |
| OpenRouterDefaultError | 4XX, 5XX | */* |
```

--------------------------------

### GET /models

Source: https://openrouter.ai/docs/sdks/typescript/api-reference/models/models

This endpoint retrieves a list of all available models from the OpenRouter service. It provides details about each model that can be used for various AI tasks.

```APIDOC
## GET /models

### Description
Retrieves a list of all available models from the OpenRouter service. This endpoint provides details about each model that can be used for various AI tasks.

### Method
GET

### Endpoint
/models

### Parameters
#### Path Parameters
None.

#### Query Parameters
None.

#### Request Body
None.

### Request Example
{}

### Response
#### Success Response (200)
- **data** (array of objects) - A list of model objects.
    - **id** (string) - The unique identifier of the model.
    - **name** (string) - The human-readable name of the model.
    - **provider** (string) - The provider of the model (e.g., "OpenAI", "Anthropic").
    - **context_length** (integer) - The maximum context length supported by the model.
    - **pricing** (object) - Pricing details for the model.
        - **prompt** (string) - Cost per 1k tokens for prompts (e.g., "0.000001").
        - **completion** (string) - Cost per 1k tokens for completions (e.g., "0.000002").

#### Response Example
{
  "data": [
    {
      "id": "openai/gpt-3.5-turbo",
      "name": "GPT-3.5 Turbo",
      "provider": "OpenAI",
      "context_length": 4096,
      "pricing": {
        "prompt": "0.000001",
        "completion": "0.000002"
      }
    },
    {
      "id": "anthropic/claude-2",
      "name": "Claude 2",
      "provider": "Anthropic",
      "context_length": 100000,
      "pricing": {
        "prompt": "0.000011",
        "completion": "0.000032"
      }
    }
  ]
}

### Error Responses
- **401 Unauthorized**: `errors.UnauthorizedResponseError` - The request lacks valid authentication credentials.
- **404 Not Found**: `errors.NotFoundResponseError` - The requested resource could not be found.
- **500 Internal Server Error**: `errors.InternalServerResponseError` - An unexpected error occurred on the server.
- **4XX, 5XX OpenRouter Default Error**: `errors.OpenRouterDefaultError` - A generic error for other client or server-side issues.
```