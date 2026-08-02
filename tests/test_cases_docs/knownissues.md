# Known Issues

## Forgot Password – broken on demo site

Clicking "Forgot your password?" opens the reset form fine, but submitting a valid username (tried "Admin") just hangs on a loading state forever no error, no success, nothing.

Probably because this is a public demo environment and password reset needs to send a real email, which likely isn't set up here. Not an app bug I can actually verify or test properly, so skipping it for this project instead of automating something broken.