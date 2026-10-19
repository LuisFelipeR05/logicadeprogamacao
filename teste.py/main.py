# pyright: reportMissingImports=false
try:
    from openai import OpenAI
except ImportError as exc:
    raise RuntimeError("Instale a biblioteca 'openai' com: pip install openai") from exc

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="freellmapi-your-unified-key",
)

resp = client.chat.completions.create(
    model="deepseek/deepseek-v4-flash-0731free:free",
    messages=[{"role": "user", "content": "Say hi in five words."}],
)
print(resp.choices[0].message.content)