import subprocess

def review_prs(start, end):
    for number in range(start, end + 1):
        pr_url = f"https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/{number}"
        command = ["python", "-m", "pr_agent.cli", "--pr_url", pr_url, "review"]
        result = subprocess.run(command, capture_output=True, text=True)
        print(f"Reviewing PR {number}:")
        print(result.stdout)
        if result.stderr:
            print(f"Error reviewing PR {number}:")
            print(result.stderr)

if __name__ == "__main__":
    start_number = int(input("Enter the start number: "))
    end_number = int(input("Enter the end number: "))
    review_prs(start_number, end_number)