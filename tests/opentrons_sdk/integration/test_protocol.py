import unittest

from opentrons_sdk.protocol.protocol import Protocol
from opentrons_sdk.labware import containers, instruments



class ProtocolTestCase(unittest.TestCase):
    def setUp(self):
        Protocol.reset()
        self.protocol = Protocol.get_instance()

    def test_protocol_container_setup(self):

        plate = containers.load('microplate.96', 'A1')
        tiprack = containers.load('tiprack.p10', 'B2')

        containers_list = self.protocol.get_containers()
        self.assertEqual(len(containers_list), 2)

        self.assertEqual(containers_list[0], ((0, 0), plate))
        self.assertEqual(containers_list[1], ((1, 1), tiprack))

    def test_protocol_head(self):

        trash = containers.load('point.trash', 'A1')
        tiprack = containers.load('tiprack.p10', 'B2')

        p200 = instruments.Pipette(
            trash_container=trash,
            tip_racks=[tiprack],
            min_vol=10,  # These are variable
            axis="b",
            channels=1
        )

        instruments_list = self.protocol.get_instruments()
        self.assertEqual(instruments_list[0], ('B', p200))

    def test_protocol_microplate_wells(self):
        plate = containers.load('microplate.96', 'A1')
        tiprack = containers.load('tiprack.p10', 'B2')

        from pprint import pprint as pp

        self.assertEqual(
            plate.total_wells,
            len([well for well in plate])
        )





