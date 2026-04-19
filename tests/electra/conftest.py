import pytest


@pytest.fixture
def builder_bid_json() -> dict[str, object]:
    return {
        "version": "electra",
        "data": {
            "message": {
                "header": {
                    "parent_hash": "0x1111111111111111111111111111111111111111111111111111111111111111",
                    "fee_recipient": "0x2222222222222222222222222222222222222222",
                    "state_root": "0x3333333333333333333333333333333333333333333333333333333333333333",
                    "receipts_root": "0x4444444444444444444444444444444444444444444444444444444444444444",
                    "logs_bloom": "0x" + ("55" * 256),
                    "prev_randao": "0x6666666666666666666666666666666666666666666666666666666666666666",
                    "block_number": "777",
                    "gas_limit": "888",
                    "gas_used": "999",
                    "timestamp": "1578009841",
                    "extra_data": "0x1234",
                    "base_fee_per_gas": "10",
                    "block_hash": "0x7777777777777777777777777777777777777777777777777777777777777777",
                    "transactions_root": "0x8888888888888888888888888888888888888888888888888888888888888888",
                    "withdrawals_root": "0x9999999999999999999999999999999999999999999999999999999999999999",
                    "blob_gas_used": "11",
                    "excess_blob_gas": "12",
                },
                "blob_kzg_commitments": [
                    "0x" + ("aa" * 48),
                ],
                "execution_requests": {
                    "deposits": [
                        {
                            "pubkey": "0x" + ("bb" * 48),
                            "withdrawal_credentials": "0x" + ("cc" * 32),
                            "amount": "13",
                            "signature": "0x" + ("dd" * 96),
                            "index": "14",
                        }
                    ],
                    "withdrawals": [
                        {
                            "source_address": "0x" + ("ee" * 20),
                            "validator_pubkey": "0x" + ("ff" * 48),
                            "amount": "15",
                        }
                    ],
                    "consolidations": [
                        {
                            "source_address": "0x" + ("11" * 20),
                            "source_pubkey": "0x" + ("22" * 48),
                            "target_pubkey": "0x" + ("33" * 48),
                        }
                    ],
                },
                "value": "16",
                "pubkey": "0x" + ("44" * 48),
            },
            "signature": "0x" + ("55" * 96),
        },
    }
