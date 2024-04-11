import asyncio

async def clone_repo(url):
    repository_name = url.split('/')[-1]
    clone_command = f'git clone --depth 1 {url} {repository_name}'
    process = await asyncio.create_subprocess_shell(clone_command)
    await process.wait()

    if process.returncode == 0:
        print(f"successfully cloned {repository_name}")
    else:
        print(f"failed to clone {repository_name}")

async def main():
    urls = [
        "https://github.com/tiangolo/fastapi",
        "https://github.com/django/django",
        "https://github.com/pallets/flask",
    ]
    tasks = []
    for url in urls:
        tasks.append(clone_repo(url))
        print(type(tasks))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())