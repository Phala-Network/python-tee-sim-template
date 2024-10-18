import os
from dstack_sdk import AsyncTappdClient, DeriveKeyResponse, TdxQuoteResponse
from fastapi import FastAPI

app = FastAPI()
# endpoint = '../../tappd.sock'
endpoint = 'http://host.docker.internal:8090'

@app.get("/")
async def root():
    client = AsyncTappdClient()
    deriveKey = await client.derive_key('/', 'test')
    assert isinstance(deriveKey, DeriveKeyResponse)
    asBytes = deriveKey.toBytes()
    assert isinstance(asBytes, bytes)
    limitedSize = deriveKey.toBytes(32)
    tdxQuote = await client.tdx_quote('test')
    return {"deriveKey": asBytes.hex(), "derive_32bytes": limitedSize.hex(), "tdxQuote": tdxQuote}
