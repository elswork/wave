# Mode / Broadcast
# Launch the server in broadcast mode to synchronize browser state across users.
# ---
from telesync import Q, listen, ui, pack


async def main(q: Q):
    count = q.app.count or 0
    if 'increment' in q.args:
        count += 1
        q.app.count = count

    items = pack([ui.button(name='increment', label=f'Count={count}')])

    if count > 0:
        form = q.page['example']
        form.items = items
    else:
        q.page['example'] = ui.form_card(box='1 1 12 10', items=items)

    await q.page.push()


if __name__ == '__main__':
    listen('/demo', main, mode='broadcast')
