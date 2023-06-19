## 🚀 Performance comparison between sync and async approach
## 📝 Results
*For 10 runs: GET request on a local server*
#### Sync
Time taken:  20.445919999998296 seconds
#### Async
Time taken:  0.34013409999897704 seconds
## ⚙️ Steps to run locally
(Use a virtual env)
1. Install the requirements
```bash
pip install -r requirements.txt
```
2. Run the local server
```bash
uvicorn local_server:app
```
3. Run `synchrounous.py` and `async_httpx.py`
```bash
python synchrounous.py
python async_httpx.py
```