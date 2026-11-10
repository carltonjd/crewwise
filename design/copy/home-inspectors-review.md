# Home inspector example: copy for review (2026-11-07)

Decision: not a full switch. The site keeps its broad audience; home inspectors replace roofing as the worked example.
Fictional company: **Keystone Home Inspections**, Tampa, FL (matches the demo line's area code, (813) 993-1087).

Files:
- `src/content/pages/home-inspectors.md`: full copy for the new `/home-inspectors/` page (same structure as `/roofing/`). Written, not yet wired to a page.
- This file: the home page changes, the demo line script and the open questions.

---

## 1. Home page hero: the example call on the phone

Replaces Harbor & Lane Law. The layout and animation stay the same; only the text changes.

| Slot | Now | New |
|---|---|---|
| Site name on the phone | Harbor & Lane Law | Keystone Home Inspections (shorten to "Keystone Inspections" if it doesn’t fit at 12px) |
| Phone headline (3 short lines) | Property, / family and / business law | Home / inspections / across Tampa |
| Phone sub-line (2 lines) | Straight answers from / lawyers close to home. | Buyer, pre-listing and / wind mitigation reports. |
| Call screen status | Booking a consultation | Booking an inspection |
| Booking slip, line 1 | Consultation booked | Inspection booked |
| Booking slip, line 2 | Thu 10:00 AM | Thu 9:00 AM |
| Booking slip, line 3 | (current) | 4412 Bayshore Ct |
| Screen-reader description | …finds Harbor & Lane Law’s website… books a consultation for Thursday at 10:00 AM. | Example: a home buyer finds Keystone Home Inspections’ website on their phone and taps Call now. The company’s AI front desk answers the call and books an inspection for Thursday at 9:00 AM. |
| Caption under the hero | Example booking for Harbor & Lane Law, a fictional firm. | Example booking for Keystone Home Inspections, a fictional company. |

The headline and sub-line above the phone stay as they are.

## 2. Home page: "Built for people who can’t always pick up"

Keep two columns (each has its own cut-paper plate). The first column leads with inspectors and links to the new page.

**Column 1** (house plate, links to `/home-inspectors/`)
- Title: Home inspectors and home-service companies
- Text: You’re in an attic or under a sink when the next one calls. The AI front desk takes the details and books the job, so it doesn’t go to voicemail.

**Column 2** (unchanged)
- Title: Law, architecture and accounting firms
- Text and note stay as they are.

## 3. The `/home-inspectors/` page

Full copy is in `src/content/pages/home-inspectors.md`. Highlights:

- **H1:** Crewwise books your next inspection while you’re in the crawlspace.
- **Sub-line:** It answers buyers and agents day or night, takes the address, the size and age of the home and the add-ons they want, and books the inspection into your calendar before they call someone else.
- **Where bookings slip away:** missed calls on site, agents kept waiting, price shoppers who drift off, "when will my report be ready?" calls, old inquiries.
- **On the call:** property details (address, sq ft, year built, foundation, add-ons, end of the inspection period), who’s calling (buyer, seller or agent), and a handoff for tight deadlines, upset clients and report questions. *It never comments on a property’s condition.*
- **Busy season** (replaces Storm Mode): spring rush, calls sorted by inspection deadline. Example report with illustrative numbers, labelled.
- **Example call:** Dana, a buyer’s agent at Gulf Coast Realty, books a buyer’s inspection with termite for 4412 Bayshore Ct, Tampa. The urgent example: an inspection period ending tomorrow is transferred to the owner.
- **FAQ:** adds "Can real estate agents book through it?" and "Will it talk about what I found in an inspection?"

## 4. Smaller changes

- Audit form trade list: add **Home inspection** at the top.
- `/roofing/`: retire it, and 301 `/roofing/`, `/roofer(s)` to `/home-inspectors/`.
- `llms.txt`: list home inspectors first under home-service companies.
- New share image `og-home-inspectors.jpg` (`pnpm og`).
- `PRODUCT.md`: inspectors as the worked example; the demo line can now appear on the site.

---

## 5. Demo line script (for the front-desk platform)

Paste into the agent’s instructions where the Oak Ridge Roofing script lives now.

> You are the front desk for **Keystone Home Inspections**, a home inspection company in Tampa, Florida. This is a demo line run by Crewwise. Be warm, brief and practical.
>
> **Greeting:** "Thanks for calling Keystone Home Inspections. How can I help?"
>
> **Services:** buyer’s inspections, pre-listing inspections, new construction inspections, 4-point inspections and wind mitigation. Add-ons: radon, termite (WDO), mold, sewer scope, pool and spa.
>
> **Service area:** Tampa, Brandon, Riverview, Wesley Chapel, Lutz and Temple Terrace. For anywhere else, take their details and say the owner will call back.
>
> **For a booking, collect, one or two questions at a time:**
> 1. Caller’s name and whether they’re the buyer, the seller or an agent
> 2. If an agent: their brokerage, and the buyer’s name and number
> 3. Property address
> 4. Approximate square footage and year built
> 5. Foundation type, if they know (slab, crawlspace or basement)
> 6. Which inspection and any add-ons
> 7. When the inspection period ends
> 8. Preferred day and time. Inspections start at 8 AM or 1 PM, Monday to Saturday.
>
> Then repeat the details back, confirm the slot, and say a text confirmation will follow.
>
> **Urgent:** if the inspection period ends within 2 days, say "That’s a tight deadline. Let me put you through to the owner," and transfer.
>
> **Common questions:**
> - Reports: delivered within 24 hours of the inspection, by email.
> - How long it takes: about 2 to 3 hours for a typical home. The buyer is welcome to join for the last 30 minutes.
> - Payment: due before the report is released.
>
> **Never:**
> - comment on a property’s condition, explain a report finding, or say whether a home is a good buy
> - recommend contractors or give repair costs
> - promise a price unless it’s in your price list (see below)
>
> **If asked whether you’re an AI:** "Yes, I’m an AI assistant. This is a Crewwise demo line, so Keystone Home Inspections is a sample business and nothing is actually booked."
>
> **Optional, only if you confirm quoting (see question A):** Sample prices: under 2,000 sq ft, $375; 2,000 to 3,000 sq ft, $450; over 3,000 sq ft, $525. Homes built before 1980 add $50. Termite $95, radon $150, sewer scope $175. Wind mitigation $125, 4-point $100, or $200 together.

---

## Open questions

- **A. Quoting:** can the front desk quote from a price list? If yes, I’ll add "Gives your standard prices on the call" to the page and keep the sample prices in the demo script. Until then, the page doesn’t claim it.
- **B. Scheduling software:** does it book into Spectora, ISN or HomeGauge, or only into Google or Outlook calendars? The page currently says "books into your calendar."
- **C. Texting the agent as well as the buyer:** possible? The page currently mentions a single text confirmation.
- **D. Demo number on the site:** OK to show (813) 993-1087 on `/home-inspectors/` as "Call and try to book an inspection" once the script is switched?
