import smartpy as sp

class Unpack(sp.Contract):
    def __init__(self):
        self.init(
            amount=sp.nat(1), 
            address=sp.address("tz1eKCEjV4aFSo5BXUCktkN9NJtDyvRF2wxS"), 
            token_id=sp.nat(0)
        )
    @sp.entry_point
    def unpack_call(self, sig, data_bytes):
        sp.set_type(sig, sp.TSignature)
        sp.set_type(data_bytes, sp.TBytes)
        k = sp.key("edpkuKYJd4SMv4eyxeQ7CDnL43XMu7itdVvjUNgowWLTrm5YtFa5Qt")
        s = sig
        b = data_bytes
        
        sp.verify(sp.check_signature(k, s, b), message = "Signature is not valid")
        data = sp.unpack(b, sp.TPair(sp.TPair(sp.TAddress, sp.TNat), sp.TNat))

        sp.trace(sp.snd(data.open_some()))

@sp.add_test(name="Unpack data")
def test():
    scenario = sp.test_scenario()
    unpack = Unpack()
    scenario += unpack
    scenario += unpack.unpack_call(
        sig=sp.signature("edsigtbMEnu61ZG4Dds7ndtGhbtaM3p2DRWfHEVQX3h6K8kbmiiG2pLWgNSgQng78rrjSpnR4ADAMRckbkjDJNXDuy2j4AgAxMt"),
        data_bytes=sp.bytes("0x05070707070a0000001600008f142637d0360ef8016effc36706f1e10d57866a000a0000")
    )




