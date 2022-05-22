# Service Engineer Coding Exercise: Madlibs

This exercise asks you to build and prepare to operationalize a microservice that generates random "madlib" sentences by fetching data from a third-party API.

The service should be self-contained and as near to deployment ready as possible.

## Requirements:

1. In any language/library/framework of your choosing, build a small service that serves a single REST endpoint (`/madlib`). This endpoint should return a templated "madlib" sentence:

> It was a {adjective} day. I went downstairs to see if I could {verb} dinner. I asked, "Does the stew need fresh {noun}?"

Feel free to use your own templated madlib sentence, but keep in mind that we need to use at least one adjective, verb, and noun.

The randomized words should be fetched from `https://reminiscent-steady-albertosaurus.glitch.me/`. There are three separate routes per part of speech: `/adjective`, `/verb`, and `/noun`.

2. Your service should be prepared for deployment by providing a `Dockerfile`. The resulting docker image should serve your API automatically when started.

3. Your service should provide tests to ensure it is working correctly. The number, thoroughness, and type of tests you provide is up to you!


When complete, push your work to a Git repository and provide us with a link to your work for discussion during the interview.

Be prepared to explain motiviations behind overall design of your service, deployment techniques, and testing strategy.