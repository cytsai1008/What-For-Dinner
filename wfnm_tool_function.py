import json
import os
import redis


# import load_command


def redis_client() -> redis.Redis:
    """Returns redis client"""
    return redis.Redis(
        host=os.environ["REDIS_WFNM_URL"],
        port=16704,
        username=os.environ["REDIS_USER"],
        password=os.environ["REDIS_WFNM_PASSWD"],
        decode_responses=True,
    )


def read_json(filename) -> dict:
    client = redis_client()
    return client.json().get(filename)


def new_read_json(filename) -> dict:
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def write_json(filename, data) -> None:
    """Writes dictionary to redis json (key: filename, value: data)"""
    redis_client().json().set(filename, ".", data)
    # return False if args is type(None)


def check_args_zero(args, arg_list) -> bool:
    return args in arg_list


def id_check(self) -> str:
    try:
        server_id = str(self.guild.id)
    except:
        server_id = f"user_{str(self.author.id)}"
    return server_id


def check_args_one(args) -> bool:
    return args is not type(None)
    # return False if args is type(None)


def check_dict_data(data: dict, arg) -> bool:
    try:
        print(f"data in {arg} is {data[arg]}")
    except KeyError:
        return False
    else:
        return True


def check_duplicate_data(existing_data, new_data: list) -> list:
    # sourcery skip: for-index-replacement
    del_key = []
    for i in range(len(existing_data)):
        for j in range(len(new_data)):
            if existing_data[i] == new_data[j]:
                del_key.append(new_data[j])
    return del_key


def check_file(filename) -> bool:
    """Check if filename exist in redis key"""
    return bool(redis_client().exists(filename))


"""
def lang_command(lang: str, command: str) -> str:
    try:
        command_out = load_command.read_description(lang, command)
    except FileNotFoundError:
        command_out = load_command.read_description("en", command)
    finally:
        return command_out
"""

# TODO: time commands function
# TODO: Merging functions to wfnm_main.py
