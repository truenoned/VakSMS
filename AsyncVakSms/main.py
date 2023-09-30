import aiohttp

class VakSmsApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://vak-sms.com/api/"

    async def get_balance(self):
        async with aiohttp.ClientSession() as session:  
            url = f"{self.base_url}getBalance/?apiKey={self.api_key}"
            async with session.get(url) as response:
                if response.status == 200:
                    return (await response.json())["balance"]
                else:
                    raise Exception(response.status)

    async def get_count_number(self, service, country, operator):
        async with aiohttp.ClientSession() as session:  
            url = f"{self.base_url}getCountNumber/?apiKey={self.api_key}&service={service}&country={country}&operator={operator}&price"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(response.status)

    async def get_number(self, service, country, operator):
        async with aiohttp.ClientSession() as session:  
            url=f"{self.base_url}getNumber/?apiKey={self.api_key}&service={service}&country={country}&operator={operator}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(response.status)

    async def prolongNumber(self, service, tel):
        async with aiohttp.ClientSession() as session:  
            url=f"{self.base_url}prolongNumber/?apiKey={self.api_key}&service={service}&tel={tel}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(response.status)

    async def get_sms(self, idNum):
        async with aiohttp.ClientSession() as session:  
            url=f"{self.base_url}getSmsCode/?apiKey={self.api_key}&idNum={idNum}&all"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Ошибка при получение SMS: {response.status}")

    async def change_status(self, idNum, status):
        async with aiohttp.ClientSession() as session:  
            url=f"{self.base_url}setStatus/?apiKey={self.api_key}&status={status}&idNum={idNum}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(response.status)