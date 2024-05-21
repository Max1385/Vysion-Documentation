Admin Commands
=================

All commands that only server admins of the Discord server can use are listed here.

Autoreaction
-------

.. hint::
    - With Autoreaction, you can specify the channel in which the bot should react automatically (with an emoji).

Setting the Autoreaction
~~~~~~~~~~

- You can use ``/autoreaction set [channel] [emoji]`` to select in which channel and with which emoji the automatic reaction should take place.

Deleting the Autoreaction
~~~~~~~~~~

- Do you want to delete the autoreaction in a channel? No Problem! You can use ``/autoreaction remove [channel]`` to remove the automatic reaction in a channel.

Counting
-------

- With Counting you can create a counting game in which channel you can then count to infinity.

Define a counting channel and number, from which you start counting
~~~~~~~~~~

- You can use ``counting set [channel]`` to define in which channel the counting game should be started.

.. warning::
    - So that the game works properly, you must set a **number from which to count before**!
    - You can do this by using the ``/counting configure [number]`` command.

Deleting the counting channel (and with it the entire game)
~~~~~~~~~~
- To delete the counting game, run ``/counting remove`` as a administrator in a discord channel.

.. note::
    - The counting game will now be deleted. After that, you must delete the discord channel.

Invite-Info
------------

- Using the invite-info command, you can get information about a custom Discord invite (e.g. discord.gg/123456789).
- To get information about a `custom invite link`, you can run ``/invite-info [invite]`` in a discord channel.

Language
------------

- With the language command you can set up the language the bot respond in your server.
- To see how it works, please take a look here: :doc:`/introduction`

Log Messages
------------

- With the Log-Messages command you can save a certain number of messages from the channel as a transcript.
- To log, or rather save messages from a discord channel, you can use ``/log-messages [amount]``.
- The bot then sends you an html file (which is deleted immediately because it is "unimportant" for the user) and an embed with a link that you can click on. The link to the online transcript will now open in your internet browser.

.. hint::
    - For the progammers: The `chat exporter <https://pypi.org/project/chat-exporter/>`_ module is used here.

Survey
------------

- With the poll command, you can easily create polls for your community to vote in.
- You can use ``/survey [question] [option_1] [option_2] [etc.]`` to create a survey with your community in the channel, `in which you executed the command`.

.. note::
    - This feature was programmed when Discord's own "Poll" function did not yet exist. The function is nevertheless left in the bot, as it is still a cool feature and correctly shows the percentages in the poll. :D

Ticketsystem
-------

- With the ticket commands you have the opportunity to set up a fully working ticket system for your Discord server!

.. hint::
    **Important features of the ticket system:**
    - Online transcript logs
    - Two options to close tickets.
    - The user can describe his support request in great deatail using our modal function.

Setup the Ticketsystem in your server
~~~~~~~~~~

- 1. **Ticket Category**: The category in which the tickets are created
- 2. **Ticket Channel**: The channel into which the ticket panel can later be sent.
- 3. **Log Channel**: The channel to which all ticket logs are sent
- 4. **Staff Role**: The role which ticket actions (e.g. accessing the ticket or closing the ticket) can be performed.
- 5. **Embed Description**: The description of the embed from the ticket panel.
- Use the command ``/ticket setup [category] [ticket_channel] [log_channel] [staff_role] [embed_description]`` to setup it in your own server.

.. note::
    - The link to a transcript is sent to the log channel so that the messages can still be read after the ticket has been deleted.

Send the Ticketpanel
~~~~~~~~~~

- To send the Ticketpanel, run following command in a channel: ``/ticket send``

.. hint::
    - Now the bot should send the panel message with your own set text (at /ticket setup -> embed_description) to your specified channel.

Delete the Ticketsystem
~~~~~~~~~~

- If you want to delete the ticket system from your server so that it no longer works, run the following command in a Discord channel: ``/ticket delete``
- All data (except for the previous ticket logs) will of course be deleted from our system.

Verifysystem
-------

- With the help of our Verify system, users can easily be verified in your server by entering a randomly generated four-digit number and receive a role (which was of course determined by you).

Setup the Verifysystem
~~~~~~~~~~
- You can set up the verification system with ``/verify setup [role]``.  Enter the role that the user should be assigned in your server after successful verification.

Send the Verifysystem
~~~~~~~~~~

- To send the verification system, please use ``/verify send [channel]``. Enter the channel, in which the verification system should be sent.

Delete the Verifysystem
~~~~~~~~~~

- To delete the verification system, use ``/verify remove``.

Welcomer
-------

- With our Welcomer system you can welcome new members via Discord Image. The good thing about it is that you can even choose the color of the image yourself.

.. warning::
    - If you have selected a color at ``/welcome set [channel] [color]`` that you no longer like after a certain time, you cannot change it directly. You have to set up the Welcomer system again. So first remove/deactivate it from your server and then set it up again.

Setup the Welcomer
~~~~~~~~~~

- To set up the welcome system, please use ``/welcome set [channel] [color]``.  As the channel, enter the channel in which new members are welcomed. For the color, enter the color you want the welcome image to have.

.. note::
    - At the moment you can choose between 6 different colors: Purple, Green, Red, Blue, Blurple (discord's color) and even Yellow!

Remove the Welcomer
~~~~~~~~~~

- To deactivate the welcome system, simply use ``/welcome remove``.
