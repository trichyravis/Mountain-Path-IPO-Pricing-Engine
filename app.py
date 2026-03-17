
ValueError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/mountain-path-ipo-pricing-engine/app.py", line 985, in <module>
    st.dataframe(
    ~~~~~~~~~~~~^
        demand_display.style.apply(highlight_cutoff, axis=1),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        use_container_width=True, hide_index=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 532, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/arrow.py", line 725, in dataframe
    marshall_styler(proto.arrow_data, data, default_uuid)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/lib/pandas_styler_utils.py", line 65, in marshall_styler
    styler._compute()  # type: ignore
    ~~~~~~~~~~~~~~~^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/io/formats/style_render.py", line 256, in _compute
    r = func(self)(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/io/formats/style.py", line 1728, in _apply
    result = data.T.apply(func, axis=0, **kwargs).T  # see GH 42005
             ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/frame.py", line 10401, in apply
    return op.apply().__finalize__(self, method="apply")
           ~~~~~~~~^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/apply.py", line 916, in apply
    return self.apply_standard()
           ~~~~~~~~~~~~~~~~~~~^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/apply.py", line 1063, in apply_standard
    results, res_index = self.apply_series_generator()
                         ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/apply.py", line 1081, in apply_series_generator
    results[i] = self.func(v, *self.args, **self.kwargs)
                 ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/mount/src/mountain-path-ipo-pricing-engine/app.py", line 980, in highlight_cutoff
    idx = demand_df.index[demand_df['Bid Price'] == float(row['Bid Price'].replace('$','').replace(',',''))].tolist()
                                                    ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
