import subprocess


def cmd(command):
    process = subprocess.Popen(
        ["cmd", "/Q", "/K", "echo off"],
        encoding='cp932',
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    process.stdin.write(command)
    process.stdin.write("\n")
    process.stdin.close()

    lines = []

    process.wait()
    while True:
        line = process.stdout.readline()
        if line:
            lines.append(line.strip())

        if not line and process.poll() is not None:
            break
    return "\r\n".join(lines)
