# Fullfilled Foods Revenue CRM / Outreach Notes

Use when Lorenzo asks to build or manage a CRM/lead database for Fullfilled Foods revenue growth.

## Revenue streams

Track leads by these lanes:

1. **Premium family weekly meal program / home food support**
   - Busy premium Miami families.
   - Offer: chef-prepared weekly meals, seasonal produce boxes with in-season fruits and vegetables, dairy, pantry staples, dry goods delivered home.
   - Tone: warm parent-to-parent when using school/community relationships.

2. **Corporate / office food programs**
   - Family offices, law firms, finance, real estate, luxury offices, cruise/hospitality HQs.
   - Offer: recurring office lunches, executive meals, meetings, wellness lunches, pantry/snack support.
   - CTA: sample drop, not long explanation.

3. **White-label wellness partnerships**
   - Gyms, pilates/yoga studios, med spas, wellness clinics, nutritionists, concierge doctors, residential buildings.
   - Offer: `[Partner] weekly wellness menu, powered by Fullfilled`.

4. **Luxury/private hospitality support**
   - Yacht managers, private aviation, estate/villa managers, concierges, luxury residences/hotels/clubs.
   - Offer: VIP culinary fulfillment, provisioning, fridge stocking, residence amenities.

5. **Premium home food support add-ons / suppliers**
   - Specialty grocery, bakery, dairy, produce, pantry partners.
   - Offer/angle: source partnerships for seasonal produce boxes and home food support.

## CRM schema

Recommended columns:

```text
lead_id
revenue_stream
segment
company_or_household
contact_name
contact_title
email
phone
website
address
neighborhood
city
priority
priority_score
pitch_angle
suggested_cta
source
source_url
status
last_touch_date
next_action
next_action_date
notes
```

## Public lead sourcing workflow

- Use public business listings/maps for B2B leads. OpenStreetMap/Overpass is acceptable for initial phone/website/address enrichment.
- Verify decision-maker/contact details before sending outreach; OSM often lacks direct emails.
- Keep public business leads separate from sensitive community/family leads.
- For school/community directory data: individual sends only; no BCC/group email blasts; no child data; no recipient child grades/classes.

## Prioritization

Score higher for:
- Premium neighborhoods: Coconut Grove, Coral Gables, Key Biscayne, Brickell, Miami Beach, Pinecrest.
- Available phone/website/email.
- Strong fit with recurring program or partner distribution.

## Messaging rules

- Families: short, permission-based CTA — “If this could be useful for your household, I’d be happy to send more details.”
- Corporate: “Could I bring a small sample drop next Tuesday or Wednesday?”
- Wellness: “Could we test a small weekly wellness menu for your members or clients?”
- Luxury/private hospitality: “Can I send over a short VIP culinary support menu for your clients/residents?”

## File convention

When creating CRM exports locally, use a folder like:

```text
~/Downloads/fullfilled_foods_crm/
```

Recommended files:

```text
fullfilled_foods_crm_master.csv
fullfilled_foods_public_business_leads.csv
fullfilled_foods_family_parent_leads_import.csv
corporate_office_food_programs.csv
white_label_wellness_partnerships.csv
luxury_private_hospitality_support.csv
premium_home_food_support_add_ons.csv
premium_family_weekly_meal_program_home_food_support.csv
README_summary.txt
```
