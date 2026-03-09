# 人工智能-游戏-测试-转换
12周AI转型计划 | 游戏测试垂直领域 | 从Python零基础到游戏AI测试工程师

## 项目进度
| 阶段 | 周数/天数 | 完成状态 | 核心成果 |
|------|-----------|----------|----------|
| 筑基攻坚期 | Day01 | ✅ 已完成 | 游戏登录模块自动化测试脚本+HTML可视化测试报告 |

## Day01 核心内容
- 完成 Python 3.10.14 环境搭建 + 虚拟环境配置；
- 基于 Pytest 编写游戏登录模块8个测试用例，覆盖：
  - 正常登录场景
  - 密码错误登录场景
  - 空用户名/空密码拦截场景
  - 非法用户名批量校验场景
- 生成可视化 HTML 测试报告，所有用例通过率100%。

## 快速运行
```bash
# 克隆仓库
git clone https://github.com/Huaixu403/人工智能-游戏-测试-转换.git
cd 人工智能-游戏-测试-转换

# 创建并激活虚拟环境（Windows）
python -m venv venv
venv\Scripts\activate.bat

# 安装依赖
pip install pytest pytest-html

# 运行登录测试，生成报告
pytest test_login.py -v --html=login_test_report.html
