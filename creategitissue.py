from github import Github
#import asyncio

# no need to try since we know it exists
username = 'TurtleDiscordIssueBOT'
password = open('password.txt').read()

g = Github(username, password) # log into github my g

async def createissue(ctx, bot):

    await ctx.send("Making issue...")
    
    if bot.__TEST_MODE:
        github_repo = g.get_repo("Soja8/test")
    else:
        github_repo = g.get_repo(f"TurtleCoin/{bot.repo_name}")

    user_info = await bot.fetch_user(bot.issue_maker_author)
    full_username = f"@{user_info.name}#{user_info.discriminator}"

    # add author info and note to the bdoy
    bot.issue_body = f"**Issue made through Discord Bot** \n\n---\n{bot.issue_body} \n\n---\n**Author**: {full_username}\n**Id**: {bot.issue_maker_author}"
    
    try:
        made_github_issue = github_repo.create_issue(title=bot.issue_title, body=bot.issue_body)
    except Exception as e:
        await ctx.send("Error! {e}".format(e))
        return False
    
    github_issue_number = made_github_issue.number
    
    if bot.__TEST_MODE:
        github_issue_link = f"https://github.com/soja8/test/issues/{github_issue_number}"
    else:
        github_issue_link = f"https://github.com/TurtleCoin/{bot.repo_name}/issues/{github_issue_number}"
    
    return github_issue_link