# import argparse
# from selfmodifai.gpt4_agent.agents.gpt_4_training_editor_agent.gpt4_training_editor_agent import (
#     gpt4_training_editor_agent,
# )
# from selfmodifai.gpt4_agent.agents.gpt_4_researcher_agent import gpt4_reseacher_agent


# def cli_parser():
#     sm_parser = argparse.ArgumentParser(description="Autonomous AI agents modifying the training code of ML models")

#     sm_parser.add_argument("agent", action="store", choices=["researcher", "editor"], help="Agent type")

#     args = sm_parser.parse_args()

#     agent = args.agent
#     agents = {"researcher": gpt4_training_editor_agent, "editor": gpt4_reseacher_agent}

#     chosen_agent = agents[agent]
#     chosen_agent()
