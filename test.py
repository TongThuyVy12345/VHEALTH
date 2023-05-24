import click
from datetime import datetime

@click.command()
@click.option('--date', prompt='Enter a date (DD-MM-YYYY)', help='The date to process')
def process_date(date):
    try:
        date_obj = datetime.strptime(date, '%d-%m-%Y')
        click.echo(f'Selected date: {date_obj}')
        # Xử lý logic của ứng dụng với đối tượng datetime được chọn
    except ValueError:
        click.echo(f'Invalid date format: {date}')

if __name__ == '__main__':
    process_date()
