from django.core.management.base import BaseCommand
from hotel.models import Room
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seed the database with rooms'

    def handle(self, *args, **kwargs):
        # Clear existing rooms
        Room.objects.all().delete()

        rooms = [
            {
                'number': '101',
                'room_type': 'single',
                'description': 'Cozy single room with a city view, perfect for solo travelers. Features a comfortable single bed, work desk, and modern amenities.',
                'price': Decimal('99.99'),
                'image': 'rooms/single.jpg',
                'is_available': True
            },
            {
                'number': '102',
                'room_type': 'double',
                'description': 'Spacious double room with a queen-size bed, ideal for couples. Includes a seating area and panoramic windows.',
                'price': Decimal('149.99'),
                'image': 'rooms/double.jpg',
                'is_available': True
            },
            {
                'number': '201',
                'room_type': 'suite',
                'description': 'Luxury suite with separate living area, king-size bed, and premium amenities. Perfect for extended stays or special occasions.',
                'price': Decimal('299.99'),
                'image': 'rooms/suite.jpg',
                'is_available': True
            },
            {
                'number': '202',
                'room_type': 'single',
                'description': 'Modern single room with garden view. Features a comfortable single bed and compact work space.',
                'price': Decimal('89.99'),
                'image': 'rooms/single2.jpg',
                'is_available': True
            },
            {
                'number': '301',
                'room_type': 'double',
                'description': 'Elegant double room with balcony and city skyline view. Includes a mini bar and lounge area.',
                'price': Decimal('179.99'),
                'image': 'rooms/double2.jpg',
                'is_available': True
            }
        ]

        for room_data in rooms:
            Room.objects.create(**room_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded rooms'))
