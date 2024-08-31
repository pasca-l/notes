# gRPC Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [What gRPC is](#what-grpc-is)
- [Writing a proto file](#writing-a-proto-file)

## What gRPC is
Having the program below, this can be described as "the `main` function calling the `hello` procedure", which is an example of a procedure call. RPC (Remote Procedure Call), is the idea of doing such procedure call remotely. [gRPC](https://grpc.io/docs/what-is-grpc/) is one implementation of RPC by Google developed in 2015.
```go
package main

func main() {
  res := hello("gRPC")
  fmt.Println(res)
}

func hello(name string) string {
  return fmt.Sprintf("Hello, %s!", name)
}
```

There are 2 major technologies that implement gRPC: HTTP/2, and Protocol Buffers. HTTP/2 is used for its POST request to send information about which procedure to call from the client, and the returning value from the server ([official doc on HTTP/2 framing for gRPC](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md)). Protocol Buffers is used to serialize the content of the request, instead of using plain text.

There are 4 communication method on gRPC: unary, server streaming, client streaming, and bidirectional streaming. Unary RPC is a one-request-one-response method. Server streaming RPC is the method where one request is given for a stream of sequence of messages, and vice versa for client streaming RPC. Bidirectional streaming RPC is the method where both sides read and write with two independently operating streams.

gRPC's stream is implemented by HTTP/2 protocol. The start and end of streaming is managed by sending HEADERS frame at the beginning and the end, and the content is sent via multiple DATA frames.

Because gRPC does not require to be aware of being implemented over HTTP, the status given back by HTTP is always 200. There is a set of gRPC error status, defined by the [grpc code package](https://pkg.go.dev/google.golang.org/grpc/codes).

## Writing a proto file
Proto files needs to be created with a `.proto` file syntax, using the [official Language Specification](https://protobuf.dev/reference/protobuf/proto3-spec/). Types other than the built-in types, ["Well Known Types"](https://protobuf.dev/reference/protobuf/google.protobuf/) such as `Timestamp`, are provided by `google.protobuf`, and can be used by importing this package.

```
// version of proto (default set to "proto2")
syntax = "proto3";

// path to place generated go code
// "PATH;PACKAGE_NAME" notation can be used to name generated go package
option go_package = "pkg/grpc;hello";

// package declaration
// package can be used for referencing types across files
package hello;

// service definition
service GreetingService {
  // service method definition
  rpc Hello (HelloRequest) returns (HelloResponse);
}

// type definition
message HelloRequest {
  string name = 1;
}

message HelloResponse {
  string message = 1;
}
```
