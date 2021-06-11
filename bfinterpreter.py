
[
    # Controller@
    (
        (None)
        if "exit" in env
        else
        (
            env["lifecycles"].__setitem__(0, ["input your brainfxck code to run:\n"]) # init lifecycle 0 <- [str ...]
            and 0 or
            [
                # Main@
                None
                if not (env["lifecycles"].__setitem__(1, [1]) # init lifecycle 1 <- [int 0]
                    and 0 or
                    env.__setitem__("code", list(input(i0)))
                    and 0 or
                    [
                        # BFComp@
                        env["vars"].__setitem__("retval",(
                            print("\ncode executed.") or -1
                            if env["pointer"]["code"] >= len(env["code"])
                            else None) or 
                            #print(env["pointer"]["code"],env["code"][env["pointer"]["code"]],env["pointer"]["memory"], env["memory"][:10], len(env["lifecycles"][1])-1) or

                            (
                                env["memory"].extend([0 for i in range(100)]) #or print("info:memory depleted") 
                                or 0
                                if env["pointer"]["memory"] >= len(env["memory"])
                                else None
                            ) or 

                            (
                                env["pointer"].__setitem__("memory", env["pointer"]["memory"]+1) or 1
                                if env["code"][env["pointer"]["code"]] == ">" 
                                else None
                            ) or 

                            (
                                env["pointer"].__setitem__("memory", env["pointer"]["memory"]-1) or 2
                                if env["code"][env["pointer"]["code"]] == "<" 
                                else None
                            ) or

                            (env["pointer"].__setitem__("memory", env["pointer"]["memory"]-1) or 3
                            if env["code"][env["pointer"]["code"]] == "<" 
                            else None) or

                            (
                                env["memory"].__setitem__(env["pointer"]["memory"], (env["memory"][env["pointer"]["memory"]]+1)%256 ) or 4
                                if env["code"][env["pointer"]["code"]] == "+" 
                                else None
                            ) or

                            (
                                env["memory"].__setitem__(env["pointer"]["memory"], (env["memory"][env["pointer"]["memory"]]-1)%256 ) or 5
                                if env["code"][env["pointer"]["code"]] == "-" 
                                else None
                            ) or

                            (
                                print(chr(env["memory"][env["pointer"]["memory"]]),end='') or 6
                                if env["code"][env["pointer"]["code"]] == "." 
                                else None
                            ) or

                            (
                                env["memory"].__setitem__(env["pointer"]["memory"], int(input(":")) ) or 7
                                if env["code"][env["pointer"]["code"]] == "," 
                                else None
                            ) or

                            (
                                (
                                    env["pointer"].__setitem__("code", 
                                        env["lifecycles"][2].append(env["pointer"]["code"]+1) or 
                                        env["vars"].__setitem__("br",1) or
                                        [   
                                            (
                                                i2-1 
                                                if env["vars"]["br"] == 0 
                                                else 
                                                (
                                                    1 
                                                    if env["lifecycles"][2].append(i2+1) 
                                                    else 
                                                        env["vars"].__setitem__("br",env["vars"]["br"]+1) 
                                                        if env["code"][i2] == "[" 
                                                        else 
                                                        (
                                                            env["vars"].__setitem__("br",env["vars"]["br"]-1) 
                                                            if env["code"][i2] == "]" 
                                                            else None
                                                        )
                                                )
                                            ) 
                                            for i2 in env["lifecycles"][2]
                                        ][-1]
                                    )
                                if env["memory"][env["pointer"]["memory"]] == 0 
                                else None
                                ) or 
                                env["lifecycles"][2].clear() or 8
                                if env["code"][env["pointer"]["code"]] == "[" 
                                else None
                            ) or

                            (
                                (
                                    env["pointer"].__setitem__("code", 
                                        env["lifecycles"][2].append(env["pointer"]["code"]-1) or 
                                        env["vars"].__setitem__("br",1) or
                                        [
                                            (
                                                i2+1 
                                                if env["vars"]["br"] == 0 
                                                else 
                                                (
                                                    1 
                                                    if env["lifecycles"][2].append(i2-1) 
                                                    else 

                                                        env["vars"].__setitem__("br",env["vars"]["br"]-1) 
                                                        if env["code"][i2] == "[" 
                                                        else 
                                                        (   
                                                            env["vars"].__setitem__("br",env["vars"]["br"]+1) 
                                                        if env["code"][i2] == "]" 
                                                            else None
                                                        )
                                                )
                                            )
                                            for i2 in env["lifecycles"][2]
                                        ][-1]
                                    )
                                    if not env["memory"][env["pointer"]["memory"]] == 0 
                                    else None
                                ) or 
                                env["lifecycles"][2].clear() or 9
                            if env["code"][env["pointer"]["code"]] == "]" 
                            else None
                            ) 
                        ) or 
                        (
                            None 
                            if env["vars"]["retval"] == -1 
                            else 
                            env["lifecycles"][1].append(1) or env["pointer"].__setitem__("code", env["pointer"]["code"]+1)
                        )

                        for i1 in env["lifecycles"][1]
                    ][-1] or env["lifecycles"][1].clear())
                else 
                (env["lifecycles"][0].append(i0))

                for i0 in env["lifecycles"][0]
            ] and env["lifecycles"][0].clear() #or print(env["memory"])
        )
    )

    for env in [
        {"vars":{},"lifecycles": [[] for i in range(3)], "code": [], "memory": [], "pointer": {"code": 0, "memory": 0}},
        {"exit": 1}
    ]
]
