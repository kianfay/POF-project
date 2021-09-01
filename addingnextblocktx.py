from sendingrawtx import instruct_wallet

answer = instruct_wallet("getblockhash", [2])
print(answer)

methodAndParams = [
    ['createrawtransaction', 
        [
            [{"txid":"bf0a1ff2bd50bc02d391c25ccd3cba7458032ddbf45a9ced1375d2b9e5b82bfa", "vout":0}], 
            [{"data":"00010203"},{"bcrt1q0n6gls7nt336nu2y7negu3fy9c2qqkfd560eh7":"1"}]
        ],
    ]
]

answer = instruct_wallet(methodAndParams[0][0], methodAndParams[0][1])
print(answer)