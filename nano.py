import json
import requests
import click

@click.group()
def group():
    pass

@group.command(help="Reads a feed.")
@click.argument("url")
def read(url):
    feed = json.loads(requests.get(url + "/nanoblog").text)
    click.echo(str(len(feed)) + " posts on " + url)
    for item in feed:
        click.echo(item["date"] + " - " + item["content"])

@group.command(help="Creates a new post.")
@click.argument("url")
@click.argument("content")
def post(url, content):
    username = input("Username: ")
    password = input("Password: ")
    if requests.post(url + "/post", data={'content': content}, auth=(username, password)).ok:
       click.echo("Successfully made a post!")
    else:
       click.echo("Couldn't make a post.")

@group.command(help="Edits an existing post.")
@click.argument("url")
@click.argument("content")
@click.argument("postid")
def edit(url, content, postid):
    username = input("Username: ")
    password = input("Password: ")
    if requests.post(url + "/edit?id=" + postid, data={'content': content}, auth=(username, password)).ok:
       click.echo("Post #" + postid + " has been edited.")
    else:
       click.echo("Couldn't edit a post.")

@group.command(help="Deletes a post.")
@click.argument("url")
@click.argument("postid")
def delete(url, postid):
    username = input("Username: ")
    password = input("Password: ")
    yorn = input("Are you sure? (Y/N)")
    if yorn == "y":
        if requests.get(url + "/delete?id=" + postid, auth=(username, password)).ok:
            click.echo("Post #" + postid + " has been deleted.")
        else:
            click.echo("Couldn't delete a post.")
    else:
        click.echo("Operation declined.")

group.add_command(read)
group.add_command(post)
group.add_command(edit)
group.add_command(delete)
  
if __name__ == "__main__":
   group()
