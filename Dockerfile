# See ../triqs/packaging for other options
FROM flatironinstitute/triqs:unstable-ubuntu-clang
ARG APPNAME=app4triqs

COPY requirements.txt /src/$APPNAME/requirements.txt
RUN pip3 install -r /src/$APPNAME/requirements.txt

COPY --chown=build . $SRC/$APPNAME
WORKDIR $BUILD/$APPNAME
RUN chown build .
USER build
ARG BUILD_ID
ARG CMAKE_ARGS
RUN cmake $SRC/$APPNAME -DTRIQS_ROOT=${INSTALL} -DBuild_Deps=Always $CMAKE_ARGS && make -j2 || make -j1 VERBOSE=1
USER root
RUN make install
