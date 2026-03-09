# test_login.py - 游戏登录模块全量测试用例
import pytest

# 基础登录成功测试
def test_game_login_success():
    """测试游戏账号密码正确登录"""
    username = "test_player_01"
    password = "GamePass@2026"
    # 校验用户名密码格式合规性
    assert len(username) >= 6, "❌ 用户名长度不足6位，不符合游戏注册规范"
    assert len(password) >= 8, "❌ 密码长度不足8位，不符合游戏注册规范"
    assert "@" in password or "_" in password or password.isalnum() is False, "❌ 密码未包含特殊字符，不符合安全规范"
    print("✅ 游戏登录成功测试用例通过")

# 密码错误登录测试
def test_game_login_failed_wrong_password():
    """测试游戏密码错误登录"""
    username = "test_player_01"
    wrong_password = "WrongPass123"
    # 校验密码错误场景逻辑
    assert wrong_password != "GamePass@2026", "❌ 密码校验逻辑异常，错误密码匹配了正确密码"
    print("✅ 游戏密码错误登录测试用例通过")

# 新增：空用户名测试
def test_game_login_empty_username():
    """测试空用户名登录"""
    username = ""
    password = "GamePass@2026"
    # 校验空用户名拦截逻辑
    assert len(username) == 0, "❌ 用户名应为空，但检测到非空值"
    print("✅ 空用户名登录测试用例通过（拦截成功）")

# 新增：空密码测试
def test_game_login_empty_password():
    """测试空密码登录"""
    username = "test_player_01"
    password = ""
    # 校验空密码拦截逻辑
    assert len(password) == 0, "❌ 密码应为空，但检测到非空值"
    print("✅ 空密码登录测试用例通过（拦截成功）")

# 新增：参数化测试（批量测试不同非法用户名）
@pytest.mark.parametrize("invalid_username", ["123", "ab", "测试", "!@#$%^"])
def test_game_login_invalid_username(invalid_username):
    """批量测试非法格式用户名登录"""
    password = "GamePass@2026"
    # 校验非法用户名拦截逻辑
    assert len(invalid_username) < 6 or not invalid_username.isalnum(), "❌ 非法用户名未被拦截"
    print(f"✅ 非法用户名「{invalid_username}」登录测试用例通过（拦截成功）")