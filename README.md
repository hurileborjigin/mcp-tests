# MCP Tests

## Sample Interactive Session

```bash
(mcp-tests) (base) khurlee-@Khurlees-MacBook-Pro mcp-tests % uv run server/client.py
Initializing chat....
2025-11-04 22:19:53,994 - mcp_use.telemetry.telemetry - INFO - Anonymized telemetry enabled. Set MCP_USE_ANONYMIZED_TELEMETRY=false to disable.

=========== Interactive MCP Chat ===========

Type 'exit' or 'quit' to end the conversation

Type 'clear' to clear the conversation hitory

============================================

You:hello

Assistant 2025-11-04 22:19:57,425 - mcp_use - INFO - 🚀 Initializing MCP agent and connecting to services...
2025-11-04 22:19:57,425 - mcp_use - INFO - 🔌 Found 0 existing sessions
2025-11-04 22:19:57,425 - mcp_use - INFO - 🔄 No active sessions found, creating new ones...
[11/04/25 22:19:57] INFO     Processing request of type ListToolsRequest                                                                server.py:674
[11/04/25 22:19:58] INFO     Processing request of type ListResourcesRequest                                                            server.py:674
                    INFO     Processing request of type ListPromptsRequest                                                              server.py:674
2025-11-04 22:19:58,054 - mcp_use - INFO - ✅ Created 1 new sessions
                    INFO     Processing request of type ListToolsRequest                                                                server.py:674
                    INFO     Processing request of type ListResourcesRequest                                                            server.py:674
                    INFO     Processing request of type ListPromptsRequest                                                              server.py:674
2025-11-04 22:19:58,732 - mcp_use - INFO - 🛠️ Created 4 LangChain tools from client
2025-11-04 22:19:58,732 - mcp_use - INFO - 🧰 Found 4 tools across all connectors
2025-11-04 22:19:58,732 - mcp_use - INFO - 🧠 Agent ready with tools: get_alert, get_config, review_code, debug_error
2025-11-04 22:19:58,741 - mcp_use - INFO - ✨ Agent initialization complete
2025-11-04 22:19:58,741 - mcp_use - INFO - 💬 Received query: 'hello'
2025-11-04 22:19:58,741 - mcp_use - INFO - 🏁 Starting agent execution
2025-11-04 22:19:59,800 - mcp_use - INFO - ✅ Agent finished with output
2025-11-04 22:19:59,801 - mcp_use - INFO - 🎉 Agent execution complete in 2.38 seconds
Hello! How can I assist you today?

You:weather alert in LA

Assistant 2025-11-04 22:20:10,071 - mcp_use - INFO - 💬 Received query: 'weather alert in LA'
2025-11-04 22:20:10,072 - mcp_use - INFO - 🏁 Starting agent execution
2025-11-04 22:20:11,188 - mcp_use - INFO - 🔧 Tool call: get_alert with input: {'state': 'CA'}
[11/04/25 22:20:11] INFO     Processing request of type CallToolRequest                                                                 server.py:674
[11/04/25 22:20:13] INFO     HTTP Request: GET https://api.weather.gov/alerts/active/area/CA "HTTP/1.1 200 OK"                        _client.py:1740
2025-11-04 22:20:13,117 - mcp_use - INFO - 📄 Tool result: [TextContent(type='text', text="
        Event: Wind Advisory
        Area: Northwestern Mendoc...
2025-11-04 22:20:16,311 - mcp_use - INFO - ✅ Agent finished with output
2025-11-04 22:20:16,312 - mcp_use - INFO - 🎉 Agent execution complete in 6.24 seconds
Here's a weather alert for Los Angeles:

**Event**: High Surf Advisory  
**Area**: Malibu Coast; Los Angeles County Beaches  
**Severity**: Minor  
**Description**:  
- *What*: Large breaking waves of 5 to 8 feet with dangerous rip currents.  
- *Where*: Malibu Coast and Los Angeles County Beaches, highest surf expected at west-facing beaches.  
- *When*: From 7 AM Thursday to 2 PM PST Friday.  
- *Impacts*: Increased risk for ocean drowning. Rip currents can pull swimmers and surfers out to sea. Large breaking waves can cause injury, wash people off beaches and rocks, and capsize small boats near shore. Minor coastal flooding is expected, around the time of high tide, over vulnerable low-lying coastal areas such as parking lots, beaches, and walkways.  
- *Additional Details*: High tide around 7 feet (MLLW) is expected to occur between 7 AM and 11 AM.  
- *Instructions*: Take the necessary actions to protect flood-prone property. Do NOT drive around barricades or through water of unknown depth. Remain out of the water due to dangerous surf conditions, or stay near occupied lifeguard towers. Rock jetties can be deadly in such conditions, stay off the rocks.

Be sure to stay safe and take any necessary precautions!

You:quit
Ending conversation...
(mcp-tests) (base) khurlee-@Khurlees-MacBook-Pro mcp-tests %
```
