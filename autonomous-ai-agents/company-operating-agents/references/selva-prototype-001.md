# Selva Operating Agent — Prototype 001 Reference

Session-derived blueprint for a company-managing agent using Selva Partners as the first implementation.

## Confirmed Terms

- Agent name: **Selva Operating Agent**
- Daily output: **Daily Operating Brief**
- Core value: **Value = Business Impact / Agent Attention**
- Plain value: **Reduce the time between what happens and the right response.**
- Level 3 Relationship Risk: **Soft + Solution-Oriented + Supervised**

## Daily Operating Brief Sections

Use exactly:

```text
1. What Happened
2. Why It Matters
3. What the Agent Can Do
4. What Needs Supervision
5. What We Learned
```

Example items:

```text
1. What Happened
- Chef asked for pricing on baby vegetables.
- Supplier price on heirloom tomatoes increased.
- Restaurant had a second late delivery.
- Microgreens arrived yesterday and are still in back storage.
- Hotel account has not ordered in 10 days.

2. Why It Matters
- Sales opportunity.
- Margin risk.
- Level 3 Relationship Risk.
- Spoilage/quality risk.
- Possible account drift.

3. What the Agent Can Do
- Draft quote.
- Compare supplier prices.
- Create fridge action.
- Draft check-in.
- Log late delivery issue.

4. What Needs Supervision
- Repeated late delivery response.
- Sensitive pricing change for key account.

5. What We Learned
- Route needs more buffer.
- Microgreens should move to daily priority zone on arrival.
- Account should be added to reorder watchlist.
```

## Seven Selva Operating Loops

### 1. Buyer / Sales Loop

Watches:
- quote requests
- follow-ups
- silence from important buyers
- sample opportunities
- high-value targets
- reorder signals
- relationship risk

Outputs:
- Today’s Buyer Actions
- draft quotes
- follow-up messages
- sample suggestions
- account-risk flags

### 2. Product / Market Loop

Watches:
- seasonal products
- supplier availability
- product scarcity
- margin opportunities
- competitor activity
- chef-interest products

Outputs:
- Today’s Product Opportunities
- products to push
- price/margin alerts
- substitution ideas

### 3. Buying / Supplier Loop

Watches:
- price changes
- supplier reliability
- quality history
- delivery consistency
- backup supplier needs

Outputs:
- Buying Recommendations
- reorder prompts
- supplier comparison
- quality-vs-price warnings

### 4. Order / Operations Loop

Watches:
- orders
- order changes
- missing details
- substitutions
- fragile/cold-sensitive items
- packing priorities
- repeat order mistakes

Outputs:
- Operations Watchlist
- packing/handling notes
- quality checks
- substitution flags

### 5. Inventory / Fridge Loop

Watches:
- what arrived
- perishability
- aging inventory
- cold sensitivity
- ethylene separation
- FIFO
- picking speed
- spoilage risk

Outputs:
- Fridge / Inventory Actions
- move-to-front priorities
- separate-storage instructions
- inspect/use-first prompts

Key cause/effect chain:

```text
bad fridge layout → slower picking → lower quality → more spoilage → worse buyer experience
```

Agent compression loop:

```text
detect layout risk → recommend movement → preserve quality → improve speed → protect customer trust
```

### 6. Logistics / Delivery Loop

Watches:
- delivery windows
- route timing
- repeated delays
- client delivery preferences
- driver notes
- delivery complaints

Outputs:
- Logistics Risk List
- route-buffer recommendations
- client-preference updates
- supervised client-response drafts

### 7. Learning / Process Improvement Loop

Watches repeated patterns:
- same client issue
- same supplier delay
- same product quality problem
- same quote delay
- same route issue
- same fridge layout problem
- same margin leak

Outputs:
- process changes
- new handling rules
- new delivery windows
- supplier changes
- follow-up cadence changes

## Relationship Risk Rule

```text
Agent drafts.
Human approves.
Agent logs.
Agent tracks whether it repeats.
```

Level 3 formula:

```text
Acknowledge → Own → Offer Solution → Ask Preference → Track
```

Example late-delivery response:

> “I’m sorry about that — I understand how frustrating it is when the delivery window isn’t consistent. We’ll look at this on our end, and one option is to move your drop-off earlier going forward so there’s more buffer. Would that work better for you?”

Solution types:

- Late Delivery: earlier drop-off window, text update before departure, priority route placement, buffer time, different delivery day.
- Product Unavailable: substitute product, reserve next arrival, earlier notification, similar seasonal item, split delivery.
- Quality Issue: replacement, credit, supplier check, photo confirmation, tighter inspection.
- Price Confusion: updated price list, confirm pricing before order, standing quote window, brief seasonal explanation.
- Communication Delay: preferred contact method, response expectation, assigned point person, automatic confirmation.

## First Launch Recommendation

Start narrow but complete:

```text
Buyer requests
+ supplier/product availability
+ order/delivery issues
+ relationship risk
+ daily action brief
```

Daily questions:

```text
Who should we sell to today?
What should we sell?
What needs to be bought or checked?
What could go wrong operationally?
Which clients need careful attention?
What should we learn from yesterday?
```

## Success Metrics

- time from event to correct response
- fewer missed follow-ups
- faster quotes
- fewer repeated delivery issues
- fewer relationship-risk surprises
- less spoilage
- better route reliability
- more useful daily actions completed
