    if playerRect.top < 0:
        playerSpeed[1] = random.choice((-playerSpeed[1], [1, 1]))

    if playerRect.right >= WIDTH:
        playerSpeed[0] = random.choice((-playerSpeed[0], [-1, 1]))

    if playerRect.bottom >= HEIGHT:
        playerSpeed[1] = random.choice((-playerSpeed[1], [-1, -1]))

    if playerRect.left < 0:
        playerSpeed[0] = random.choice((-playerSpeed[0], [1, -1]))



    # if playerRect.top < 0:
    #     playerSpeed = random.choice(([-1, 1], [1, 1]))

    # if playerRect.right >= WIDTH:
    #     playerSpeed = random.choice(([-1, -1], [-1, 1]))

    # if playerRect.bottom >= HEIGHT:
    #     playerSpeed = random.choice(([1, -1], [-1, -1]))

    # if playerRect.left < 0:
    #     playerSpeed = random.choice(([1, 1], [1, -1]))
