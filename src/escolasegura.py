#coding=utf-8
import streamlit as st
import yaml 
import session
import time

import pages.main as es

import utils

def main():
    # SESSION STATE
    time.sleep(
        0.05
    )  # minimal wait time so we give time for the user session to appear in steamlit
    session_state = session.SessionState.get(
        key=session.get_user_id(),
        update=False,
        state_name="Acre",
        state_num_id=None,
        city_name="Todos",
        city_id=None,
        refresh=False,
        reset=False,
        already_generated_user_id=None,
        pages_open=None,
        amplitude_events=None,
        button_styles=dict(),
        continuation_selection=None,
        button_simule = 0,
    )
    
    es.main(session_state)

if __name__ == "__main__":
    main() 