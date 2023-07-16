# ClashByte
Clash &amp; Clash.Meta 外部控制的 Python 实现

## Get started

1. Install package

   ```bash
   pip install -U clashbyte
   ```

2. hello world

   ```python
   from clashbyte import ClashMetaAPI
   
   CONTROLLER_URL = "http://127.0.0.1:9090"
   
   if __name__ == '__main__':
       clash = ClashMetaAPI()
       if clash.is_alive:
           print(f"{clash.version=}")
   ```

   
