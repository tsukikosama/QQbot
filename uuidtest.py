import uuid
import re

def validate_uuid_format(uuid_str):
    # UUID 的正则表达式
    uuid_regex = re.compile(
        r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    )
    return uuid_regex.match(uuid_str) is not None

def validate_uuid_version(uuid_str, version):
    try:
        # 尝试将字符串转换为 UUID 对象
        uuid_obj = uuid.UUID(uuid_str, version=version)
        # 校验字符串是否与生成的 UUID 对象匹配
        return str(uuid_obj) == uuid_str
    except ValueError:
        return False

# 示例 UUID 字符串
uuid_str = "748be66e-33f9-4c54-9db2-8d07b196167f"

# 校验 UUID 格式
is_format_valid = validate_uuid_format(uuid_str)
print(f"UUID '{uuid_str}' 格式校验结果：{is_format_valid}")

# 校验 UUID 版本
version = 5
is_version_valid = validate_uuid_version(uuid_str, version)
print(f"UUID '{uuid_str}' 版本 {version} 校验结果：{is_version_valid}")

if __name__ == "__main__":
    validate_uuid_version("a32a7f94ff069c8e3edfe7963f2c7987",4);
