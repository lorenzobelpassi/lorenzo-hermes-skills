# Natoora Weekly Inbounds as Brokerage Supplier Intel

Use Natoora weekly inbound PO documents to infer supplier relationships and purchase patterns for Selva’s brokerage/wholesale sourcing strategy.

## What they are

Weekly inbounds are supplier-side purchase order documents. They show product lines Natoora bought into Miami, from which suppliers, with quantities, units, PO numbers, dates, region, and goods-in status.

This is different from customer POs (Birchstreet/Adaco hotel purchase orders), which show customers buying from Natoora.

## Why they matter for Selva

Weekly inbounds reveal:

- Suppliers Natoora relied on for Miami product flow.
- Which categories were bought locally vs air vs ground vs blended market.
- Where Selva can recreate a sourcing lane.
- Which suppliers might support brokerage cash-flow volume.
- Which specialty lines can feed direct-to-chefs margin business.

## Known Week 6 supplier map

Extracted from:

`/Users/lorenzobelpassi/Library/Mobile Documents/com~apple~CloudDocs/NATOORA/WEEKLY INBOUNDS/Week 6 PO.pdf`

Top Week 6 suppliers:

- Natoora Us Inc. (NYC) - By Ground: apples, beef, beets, butter, eggs, radicchio, olive oil, winter squash, tomatoes.
- C&B Farms: beets, cabbage, herbs, eggplant, green peppers, parsley, radishes, spinach.
- Exotic Growers: cacao fruit, dragon fruit, guava, key limes, pomelo, rambutan, tamarillo.
- Naturama Foods: basil, chives, culantro, mint, Thai basil.
- Coosemans Miami: rainbow carrots, endive, marigolds, garlic, shallots, Idaho potatoes, strawberries.
- Tiny Farm: local arugula, Namwah banana, garlic chives, mizuna mix, baby heads, purple daikon, scallions, Hakurei turnips.
- Ray’s Heritage: baby bok choy, napa cabbage, sweet corn, dill, iceberg, romaine hearts.
- Ark Foods: cherry hots, Jimmy Nardello, long hots, serrano, shishito, mini heirloom tomatoes.
- County Line - Air: Selvatica arugula, baby lettuce, Little Gem, Lola Rosa, Salanova.
- Sunny Cal - Air: mandarins, blood oranges, Asian pears, tangerines.

## Recommended future automation

When new weekly inbound docs are found:

1. Extract line-level CSV.
2. Normalize supplier names.
3. Classify product categories: commodity produce, specialty produce, fruit, citrus, herbs, pantry/dry goods, meat/dairy, packaging.
4. Update Brokerage / Wholesale Pipeline with high-volume brokerable lines.
5. Update Dried Goods Opportunity Map if pantry/shelf-stable items appear.
6. Add “supplier to research/contact” actions to the daily brokerage briefing.

## Pitfall

If the user asks “where we purchased a lot of things from,” avoid replying with hotel/customer PO results. The correct artifact is usually the `WEEKLY INBOUNDS` folder/document, not purchase order emails from customers.
