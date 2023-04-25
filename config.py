host="0.0.0.0"
port = 12345
max_size = 41943040
is_multi = 0
max_conn = 30
process_dec = [
        "rm_arabic",
        "batch_encryption_201610",
        "method1",
        "method2",
        "method3",
        "method4"
]
run_process = [
        "rm_arabic(file)",
        "batch_encryption_201610(file)",
        "method1(file)",
        """method2(file,2,b'@echo off&(if defined @lo@ goto \xc2\xa1)&setlocal disableDelayedExpansion&for /f "delims=: tokens=2" %%A in (\'chcp\') do set "@chcp@=chcp %%A>nul"&chcp 708>nul&set ^"@args@=%*"',8)""",
        "method2(file,3,'''@echo off''',110)",
        "method4(file)",
]