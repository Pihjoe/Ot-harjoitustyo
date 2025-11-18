```mermaid

sequenceDiagram
    participant laitehallinto
    participant rautatientori
    participant ratikka6
    participant bussi224
    participant lippu_luukku
    participant kallen_kortti

    Main ->> laitehallinto: HKKLaitehallinto()    
    Main ->> rautatientori: Lukijalaite()
    Main ->> ratikka6: Lukijalaite()
    Main ->> bussi224: Lukijalaite()    
    Main ->> lippu_luukku: Kioski()
    
    lippu_luukku ->> kallen_kortti: osta_matkakortti("Kalle") 
    rautatientori ->> kallen_kortti: lataa_arvoa(kallen_kortti, 3)

    ratikka6 ->> kallen_kortti: osta_lippu(kallen_kortti, 0)
    ratikka6 ->> Main: True

    bussi224 ->> kallen_kortti: osta_lippu(kallen_kortti, 2)
    bussi224 ->> Main: False

