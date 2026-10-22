Title: MotoPin Privacy Policy
Date: 2026-09-30 22:24
Author: The Unbound Nomad
Category: Page
Tags: Privacy, MotoPin
Slug: motopin-privacy-policy
Status: hidden

Last updated: 10/21/2026

Welcome to MotoPin! MotoPin is a motorcycle GPS pin-dropping app built by The Unbound Nomad. This policy explains what information MotoPin collects, how it's used, and the choices you have. We've kept it short because, honestly, there isn't much to tell — MotoPin was built from the ground up to keep your data on your own phone.

## Information We Collect

**Location data.** MotoPin's entire purpose is capturing your GPS location when you tap the "PIN IT" button (from the home screen widget, Quick Settings tile, or floating button), so that we can save it as a pin for you to review later. This is precise location data (via Android's Fused Location Provider).

**Photos (optional).** If you choose to attach a photo to a pin, that photo is copied into MotoPin's private app storage on your device.

**What we don't collect.** MotoPin does not ask for your name, email address, or any account sign-up — there is no MotoPin account. MotoPin has no ads and no analytics or advertising SDKs, and we (The Unbound Nomad) never receive your device identifiers, usage statistics, or crash logs. The Google map and place-search components built into the app do send some technical information to Google; see **Google services MotoPin uses** below.

## Where Your Data Lives

This is the important part: **your pins, notes, categories, and photos are stored entirely in a local database on your phone.** MotoPin has no server, and your location data is never transmitted to us or sold. Apart from the Google and OpenStreetMap requests described below, it isn't shared with anyone. Uninstalling the app deletes this data.

The one exception is the nearby-place search MotoPin runs when you resolve a "New" pin. MotoPin sends that pin's coordinates to **Google Maps (Google Places)** to look up named places nearby; if Google can't be reached, it asks **OpenStreetMap's public Overpass service** instead. At the same time, your phone's built-in Android address lookup turns the coordinates into a street address, which may also involve Google's servers. These requests contain only the pin's coordinates, never your name, account, or other pins, and nothing is sent until you tap a New pin to resolve it. Google's and OpenStreetMap's own privacy policies govern those requests once they leave your device ([Google Privacy Policy](https://policies.google.com/privacy), [OpenStreetMap Foundation Privacy Policy](https://osmfoundation.org/wiki/Privacy_Policy)). You can always skip the search and pick a location manually instead.

## Google services MotoPin uses

MotoPin is built on a few Google components. They talk to Google directly, and Google's own [privacy policy](https://policies.google.com/privacy) governs what they send. None of it includes your pins' names, notes, or photos, and MotoPin doesn't send Google your name or Google account.

- **Google Maps (the map screens).** When you open a map, the map images for the area on screen are loaded from Google. Google's map component (Maps SDK for Android) also automatically sends Google technical information: device details such as Android version and phone model, crash reports, your IP address, and a pseudonymous identifier Google uses to count active users. ([Google's disclosure](https://developers.google.com/maps/documentation/android-sdk/play-data-disclosure))
- **Google Places (nearby-place search).** When you tap a New pin, that pin's coordinates go to Google to find nearby places, along with the same kind of technical information (request details, crash reports, IP address, and a pseudonymous identifier). ([Google's disclosure](https://developers.google.com/maps/documentation/places/android-sdk/play-data-disclosure))
- **Google Play services location.** Your phone's location service works out your GPS position when you tap Pin It.
- **Google Play (MotoPin Pro purchase).** If you buy MotoPin Pro, Google Play handles the purchase and payment. MotoPin never sees your payment details; it only remembers on your phone that Pro is unlocked, and asks Google Play to confirm the purchase when the app starts.

## How We Use Your Information

We use the location and photo data you capture solely to provide MotoPin's core features: saving pins, showing them on a map, matching new pins to real places, and letting you export or share your ride history. That's it — there's no other use, because there's no other place for it to go.

## Sharing Your Information

We do not sell, trade, or otherwise transfer your information to third parties. When you choose to use MotoPin's Share, Export, or Back Up Pins features, you are the one sending your data — to whatever app, contact, or file you pick from your phone's share sheet (for example, saving a backup to your own Google Drive). That's your action, not something MotoPin does on your behalf. Likewise, Import Pins and Restore Pins only read the file you pick.

## App Permissions

MotoPin asks for a few Android permissions, each tied directly to a feature you choose to use:

- **Location (Fine/Coarse)** — required to capture where you are when you tap "PIN IT."
- **Notifications** (Android 13+) — used only for the floating button's "floating button is on" notification and the brief "Pinning your location…" notification shown while a pin is being saved.
- **Display over other apps** — required only if you turn on the optional floating "Pin It" button, so it can appear on top of other apps.

You can deny any of these, but the related feature won't work without it.

## Children's Privacy

MotoPin is not directed at children and does not knowingly collect information from children under 13.

## Data Retention & Your Control

Your pins stay on your device for as long as you keep them. You can delete an individual pin any time (swipe to delete, with Undo), or wipe everything at once from the app's Clear All Pins menu option. Uninstalling MotoPin removes all locally stored data.

## Security

Your pin data is stored in MotoPin's private, sandboxed app storage on your device, protected by Android's own app-level security. As with any data transmission (such as the optional nearby-place search above), no method of transmission over the internet is completely secure, though the data sent in that request contains no personal or identifying information.

## Links to Other Websites / Apps

MotoPin's Share and Save-to-Google-Maps features may open other apps or websites (like Google Maps) that you choose. We aren't responsible for the privacy practices of those third-party apps and encourage you to review their own policies.

## Changes to This Privacy Policy

We may update this policy from time to time. Changes will be posted on this page with a new "Last updated" date. Continued use of MotoPin after a change means you accept the updated policy.

## Contact Us

Questions about this policy? Reach us at privacy@unboundnomad.com.

By using MotoPin, you consent to the terms outlined in this Privacy Policy.
