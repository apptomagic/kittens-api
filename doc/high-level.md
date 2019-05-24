# Kittens: a community communication hub

Kittens is a communication platform for communities of any kind of formality, business to informal, for- or non-profit. It's meant to replace tools like forums, mailing lists, and Reddit™ or *ch clones, based on more current understanding of the needs, as well as UX design and technologies.

The central component of Kittens is a published API. Web, mobile, and any other future user interfaces are implemented as equal players, as clients of this API.

## Main entities

- Conversation: a collection of Posts consisting of a root or ‘OP’, and any number of replies, belonging to at least one Topic. Could be called a ‘thread’ or ‘topic’ or ‘post’ on other systems.

- Post: a piece of text (and possible attachments) posted by a user, possibly in reply to another Post. Always part of exactly one Conversation, may be the Conversation's starting point (OP) or a reply.

- Topic: a tag that is applied to Conversations. Has at least one name, possibly translations or synonyms. Managed by the Community administrators and moderators. A Topic always belong to one and only one Community; a Community can't have two Topics with the same name *(TBD: what if translations happen to coincide in spelling?)* but different Communities can have Topics with the same name. Discovery of Conversations (browsing) happens mainly through Topics; they're the equivalent of ‘subforums’, ‘groups’, ‘subreddits’, etc, except a Conversation can (and is expected to usually) have more than one Topic.

- Subscription: while users can browse around and view all Conversations on given Topics, our expectation is that browsing will mostly be used for discovering new areas of the community, while day-to-day use will revolve around Subscriptions. Users can subscribe to Conversations or to Topics, and then have easy ways to consume content they're interested in. *(Still under consideration is the idea of excluding or muting Topics, or possibly having the whole Subscription story based on a (completely optional for the user) Usenet-like scoring system.)*

- Community: essentially a collection of Topics and Conversation. Each Topic and Conversation is associated with exactly one Community, and the UI makes Communities very clearly separated. A server admin running their own installation has the option of running it as single-Community, which doesn't change the APIs in any way but somehow makes the UI hide all Community navigation. *(Possibly we also want a preset with one public and one secret Community for admin/mod meta-talk?)* Communities include a form of access control, where a number of users are Community administrators, with a TBD number of other user levels (possibly: moderator, regular, limited; or possibly configurable with presets).

- User.

Some secondary concepts probably to be integrated:

- Reactions (single Unicode-emoji character) to individual Posts.

- Scoring/voting of Conversations and Posts (configurable on a Community basis).

- Attachments.

- Chat (real time); possible to integrate Matrix?

- Spam control.

- Bots: how to allow it, how to prevent abuse. Having the ability is certainly a good idea for some Community use cases, and comes more or less ‘for free’ with the API approach, but administrators should be able to disallow it or limit it, and abuse is a clear risk.
