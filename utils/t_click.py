'''
click.
'''
import click

@click.command()
@click.options('--count',default=1,help='numbers of greeting')
@click.options('--name',prompt='your name',help='the person to greet')
def hello(count,name):
	for x in range(count):
		click.echo('hello %s!'%name)

if __name__ == '__main__':
	hello()