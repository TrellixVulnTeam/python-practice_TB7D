# cli.py
import click

# decorator for click

@click.command()
def main():
    print("I'm a beautiful CLI ✨")

if __name__ == "__main__":
    main()