# How to Upload Your Project to GitHub

Since you already have the project files and Git installed, follow these simple steps to get your project online.

## Step 1: Create a Repository on GitHub
1. Go to [GitHub.com](https://github.com/) and sign in.
2. Click the **+** icon in the top-right corner and select **New repository**.
3. **Repository name**: Enter `job-market-analytics`.
4. **Description**: "End-to-end analytics system for job market insights (Python, SQL, Power BI)."
5. **Public/Private**: Choose **Public** (best for portfolios).
6. **Initialize this repository with**: Leave all these unchecked (we already have code).
7. Click **Create repository**.

## Step 2: Push Your Code
You will see a page with setup commands. Look for the section **"…or push an existing repository from the command line"**.

Copy and run the following commands in your terminal (Command Prompt or PowerShell) inside the project folder:

```bash
# 1. Link your local folder to GitHub
git remote add origin https://github.com/psaluja1/job-market-analytics.git

# 2. Rename the branch to main (standard practice)
git branch -M main

# 3. Push your code
git push -u origin main
```
*(Replace `YOUR_USERNAME` with your actual GitHub username)*

## Step 3: Verify
1. Refresh the GitHub page.
2. You should see all your files (`etl/`, `analysis/`, `README.md`, etc.).
3. Your beautiful `README.md` will be displayed on the main page.

## Troubleshooting
- **"Permission denied"**: You might need to log in. If prompted, enter your GitHub username and password (or Personal Access Token).
- **"Remote origin already exists"**: Run `git remote remove origin` and try again.
