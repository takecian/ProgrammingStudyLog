# Part1

https://medium.com/@duruldalkanat/ios-interview-questions-13840247a57a

## 1- How could you set up Live Rendering? 
The attribute @IBDesignable lets Interface Builder perform live updates on a particular view. IBDesignable requires Init frame to be defined as well in UIView class.
## 2- What is the difference between Synchronous & Asynchronous task? 
Synchronous: waits until the task have completed Asynchronous: completes a task in the background and can notify you when complete
## 3- Explain Compilation Conditions
Compilation Conditions to use if DEBUG … endif structure to include or disable given block of code ve separate targets.
## 4- What is made up of NSError object? 
There are three parts of NSError object a domain, an error code, and a user info dictionary. The domain is a string that identifies what categories of errors this error is coming from.
## 5- What is Enum or Enumerations?
According to Apple’s Swift documentation:
Managing state, the bits of data that keep track of how the app is being used at the moment, is an important part of a developing your app. Because enumerations define a finite number of states, and can bundle associated values with each individual state, you can use them to model the state of your app and its internal processes.
Enum is a type that basically contains a group of related values in the same umbrella but case-less enum won’t allow us to create an instance.
Reference: https://developer.apple.com/documentation/swift/maintaining_state_in_your_apps
## 6- What is the bounding box? 
The bounding box is a term used in geometry; it refers to the smallest measure (area or volume) within which a given set of points.
## 7- Why don’t we use strong for enum property in Objective-C? 
Because enums aren’t objects, so we don’t specify strong or weak here.
## 8- What is @synthesize in Objective-C? 
synthesize generates getter and setter methods for your property.
## 9- What is @dynamic in Objective-C? 
We use dynamic for subclasses of NSManagedObject. @dynamic tells the compiler that getter and setters are implemented somewhere else.
## 10- Why do we use synchronized? 
synchronized guarantees that only one thread can be executing that code in the block at any given time.
## 11- What is the difference strong, weaks, read only and copy?
strong, weak, assign property attributes define how memory for that property will be managed.
Strong means that the reference count will be increased and
the reference to it will be maintained through the life of the object
Weak ( non-strong reference ), means that we are pointing to an object but not increasing its reference count. It’s often used when creating a parent child relationship. The parent has a strong reference to the child but the child only has a weak reference to the parent.
Every time used on var
Every time used on an optional type
Automatically changes itself to nil
Read-only, we can set the property initially but then it can’t be changed.
Copy means that we’re copying the value of the object when it’s created. Also prevents its value from changing.
for more details check this out
## 12- What is Dynamic Dispatch? 
Dynamic Dispatch is the process of selecting which implementation
of a polymorphic operation that’s a method or a function to call at run time. This means, that when we wanna invoke our methods like object method. but Swift does not default to dynamic dispatch
## 13- What’s Code Coverage? 
Code coverage is a metric that helps us to measure the value of our unit tests.
## 14- What’s Completion Handler? 
Completion handlers are super convenient when our app is making an API call, and we need to do something when that task is done, like updating the UI to show the data from the API call. We’ll see completion handlers in Apple’s APIs like dataTaskWithRequest and they can be pretty handy in your own code.
The completion handler takes a chunk of code with 3 arguments:(NSData?, NSURLResponse?, NSError?) that returns nothing: Void. It’s a closure.
The completion handlers have to marked @escaping since they are executed some point after the enclosing function has been executed.
## 15- How to Prioritize Usability in Design ? 
Broke down its design process to prioritize usability in 4 steps:
Think like the user, then design the UX.
Remember that users are people, not demographics.
When promoting an app, consider all the situations in which it could be useful.
Keep working on the utility of the app even after launch.
## 16- What’s the difference between the frame and the bounds? 
The bounds of a UIView is the rectangle, expressed as a location (x,y) and size (width, height) relative to its own coordinate system (0,0). 
The frame of a UIView is the rectangle, expressed as a location (x,y) and size (width, height) relative to the superview it is contained within.
## 17- What is Responder Chain ? 
A ResponderChain is a hierarchy of objects that have the opportunity to respond to events received.
## 18- What is Regular expressions? 
Regular expressions are special string patterns that describe how to search through a string.
## 19- What is Operator Overloading? 
Operator overloading allows us to change how existing operators behave with types that both already exist. Operators are those little symbols like +, *, and /
## 20- What is TVMLKit? 
TVMLKit is the glue between TVML, JavaScript, and your native tvOS application.
## 21- What is Platform limitations of tvOS? 
First, tvOS provides no browser support of any kind, nor is there any WebKit or other web-based rendering engine you can program against. This means your app can’t link out to a web browser for anything, including web links, OAuth, or social media sites.
Second, tvOS apps cannot explicitly use local storage. At product launch, the devices ship with either 32 GB or 64 GB of hard drive space, but apps are not permitted to write directly to the onboard storage.
tvOS app bundle cannot exceed 4 GB.
## 22- What is Functions? 
Functions let us group a series of statements together to perform some task. Once a function is created, it can be reused over and over in your code. If you find yourself repeating statements in your code, then a function may be the answer to avoid that repetition.
Pro Tip, Good functions accept input and return output. Bad functions set global variables and rely on other functions to work.
## 23- What is ABI? 
ABIs are important when it comes to applications that use external libraries. If a program is built to use a particular library and that library is later updated, you don’t want to have to re-compile that application (and from the end user's standpoint, you may not have the source). If the updated library uses the same ABI, then your program will not need to change. ABI stability will come with Swift 5.0

## 24- Why is design pattern very important ? 
Design patterns are reusable solutions to common problems in software design. They’re templates designed to help you write code that’s easy to understand and reuse. Most common Cocoa design patterns:
Creational: Singleton.
Structural: Decorator, Adapter, Facade.
Behavioral: Observer, and, Memento
## 25- What is Singleton Pattern ? 
The Singleton design pattern ensures that only one instance exists for a given class and that there’s a global access point to that instance. It usually uses lazy loading to create the single instance when it’s needed the first time.
## 26- What is Facade Design Pattern? 
The Facade design pattern provides a single interface to a complex subsystem. Instead of exposing the user to a set of classes and their APIs, you only expose one simple unified API.
## 27- What is Decorator Design Pattern? 
The Decorator pattern dynamically adds behaviors and responsibilities to an object without modifying its code. It’s an alternative to subclassing where you modify a class’s behavior by wrapping it with another object.
In Objective-C there are two very common implementations of this pattern: Category and Delegation. In Swift there are also two very common implementations of this pattern: Extensions and Delegation.
## 28- What is Adapter Pattern? 
An Adapter allows classes with incompatible interfaces to work together. It wraps itself around an object and exposes a standard interface to interact with that object.
## 29- What is Observer Pattern? 
In the Observer pattern, one object notifies other objects of any state changes.
Cocoa implements the observer pattern in two ways: Notifications and Key-Value Observing (KVO).
## 30- What is Memento Pattern? 
In Memento Pattern saves your stuff somewhere. Later on, this externalized state can be restored without violating encapsulation; that is, private data remains private. One of Apple’s specialized implementations of the Memento pattern is Archiving other hand iOS uses the Memento pattern as part of State Restoration.
## 31- Explain MVC
Models — responsible for the domain data or a data access layer which manipulates the data, think of ‘Person’ or ‘PersonDataProvider’ classes.
Views — responsible for the presentation layer (GUI), for iOS environment think of everything starting with ‘UI’ prefix.
Controller/Presenter/ViewModel — the glue or the mediator between the Model and the View, in general responsible for altering the Model by reacting to the user’s actions performed on the View and updating the View with changes from the Model.
## 32- Explain MVVM 
UIKit independent representation of your View and its state. The View Model invokes changes in the Model and updates itself with the updated Model, and since we have a binding between the View and the View Model, the first is updated accordingly.
Your view model will actually take in your model, and it can format the information that’s going to be displayed on your view.
There is a more known framework called RxSwift. It contains RxCocoa, which are reactive extensions for Cocoa and CocoaTouch.
## 33- How many different annotations available in Objective-C ?
_Null_unspecified, which bridges to a Swift implicitly unwrapped optional. This is the default.
_Nonnull, the value won’t be nil it bridges to a regular reference.
_Nullable the value can be nil, it bridges to an optional.
_Null_resettable the value can never be nil, when read but you can set it to know to reset it. This is only apply property.
## 34- What is JSON/PLIST limits ?
We create your objects and then serialized them to disk..
It’s great and very limited use cases.
We can’t obviously use complex queries to filter your results.
It’s very slow.
Each time we need something, we need to either serialize or deserialize it.
it’s not thread-safe.
## 35- What is SQLite limits ?
We need to define the relations between the tables. Define the schema of all the tables.
We have to manually write queries to fetch data.
We need to query results and then map those to models.
Queries are very fast.
## 36- What is Realm benefits ?
An open-source database framework.
Implemented from scratch.
Zero copy object store.
Fast.
## 37- How many are there APIs for battery-efficient location tracking ? 
There are 3 apis.
Significant location changes — the location is delivered approximately every 500 metres (usually up to 1 km)
Region monitoring — track enter/exit events from circular regions with a radius equal to 100m or more. Region monitoring is the most precise API after GPS.
Visit events — monitor place Visit events which are enters/exits from a place (home/office).
## 38- What is the Swift main advantage ? 
To mention some of the main advantages of Swift:
Optional Types, which make applications crash-resistant
Built-in error handling
Closures
Much faster compared to other languages
Type-safe language
Supports pattern matching
## 39- Explain generics in Swift ? 
Generics create code that does not get specific about underlying data types. Don’t catch this article. Generics allow us to know what type it is going to contain. Generics also provides optimization for our code.
## 40- Explain lazy in Swift ? 
An initial value of the lazy stored properties is calculated only when the property is called for the first time. There are situations when the lazy properties come very handy to developers.
## 41- Explain what is defer ? 
defer keyword which provides a block of code that will be executed in the case when execution is leaving the current scope.
## 42- How to pass a variable as a reference ? 
We need to mention that there are two types of variables: reference and value types. The difference between these two types is that by passing value type, the variable will create a copy of its data, and the reference type variable will just point to the original data in the memory.
## 43- How to pass data between view controllers?
There are 3 ways to pass data between view controllers.
Segue, in prepareForSegue method (Forward)
Delegate (Backward)
Setting variable directly (Forward)
## 44- What is Concurrency ?
Concurrency is dividing up the execution paths of your program so that they are possibly running at the same time. The common terminology: process, thread, multithreading, and others. Terminology;
Process, An instance of an executing app
Thread, Path of execution for code
Multithreading, Multiple threads or multiple paths of execution running at the same time.
Concurrency, Execute multiple tasks at the same time in a scalable manner.
Queues, Queues are lightweight data structures that manage objects in the order of First-in, First-out (FIFO).
Synchronous vs Asynchronous tasks
## 45- Grand Central Dispatch (GCD)
GCD is a library that provides a low-level and object-based API to run tasks concurrently while managing threads behind the scenes. Terminology;
Dispatch Queues, A dispatch queue is responsible for executing a task in the first-in, first-out order.
Serial Dispatch Queue A serial dispatch queue runs tasks one at a time.
Concurrent Dispatch Queue A concurrent dispatch queue runs as many tasks as it can without waiting for the started tasks to finish.
Main Dispatch Queue A globally available serial queue that executes tasks on the application’s main thread.
## 46- Readers-Writers
Multiple threads reading at the same time while there should be only one thread writing. The solution to the problem is a readers-writers lock which allows concurrent read-only access and an exclusive write access. Terminology;
Race Condition A race condition occurs when two or more threads can access shared data and they try to change it at the same time.
Deadlock A deadlock occurs when two or sometimes more tasks wait for the other to finish, and neither ever does.
Readers-Writers problem Multiple threads reading at the same time while there should be only one thread writing.
Readers-writer lock Such a lock allows concurrent read-only access to the shared resource while write operations require exclusive access.
Dispatch Barrier Block Dispatch barrier blocks create a serial-style bottleneck when working with concurrent queues.
## 47- NSOperation — NSOperationQueue — NSBlockOperation
NSOperation adds a little extra overhead compared to GCD, but we can add dependency among various operations and re-use, cancel or suspend them.
NSOperationQueue, It allows a pool of threads to be created and used to execute NSOperations in parallel. Operation queues aren’t part of GCD.
NSBlockOperation allows you to create an NSOperation from one or more closures. NSBlockOperations can have multiple blocks, that run concurrently.
## 48- KVC — KVO
KVC adds stands for Key-Value Coding. It’s a mechanism by which an object’s properties can be accessed using string’s at runtime rather than having to statically know the property names at development time.
KVO stands for Key-Value Observing and allows a controller or class to observe changes to a property value. In KVO, an object can ask to be notified of any changes to a specific property, whenever that property changes value, the observer is automatically notified.
## 49- Please explain Swift’s pattern matching techniques
Tuple patterns are used to match values of corresponding tuple types.
Type-casting patterns allow you to cast or match types.
Wildcard patterns match and ignore any kind and type of value.
Optional patterns are used to match optional values.
Enumeration case patterns match cases of existing enumeration types.
Expression patterns allow you to compare a given value against a given expression.
## 50- Explain Guard statement
There are three big benefits to guard statement.
One is avoiding the pyramid of doom, as others have mentioned — lots of annoying if let statements nested inside each other moving further and further to the right. The second benefit is providing an early exit out of the function using break or using return.
The last benefit, guard statement is another way to safely unwrap optionals.

# Step2

https://medium.com/@duruldalkanat/50-ios-interview-questions-and-answers-part-2-45f952230b9f

## 1- Please explain Method Swizzling in Swift
Method Swizzling is a well-known practice in Objective-C and in other languages that support dynamic method dispatching.
Through swizzling, the implementation of a method can be replaced with a different one at runtime, by changing the mapping between a specific #selector(method) and the function that contains its implementation.
To use method swizzling with your Swift classes there are two requirements that you must comply with:
The class containing the methods to be swizzled must extend NSObject
The methods you want to swizzle must have the dynamic attribute
## 2- What is the difference Non-Escaping and Escaping Closures?
The lifecycle of a non-escaping closure is simple:
Pass a closure into a function
The function runs the closure (or not)
The function returns
Escaping closure means, inside the function, you can still run the closure (or not); the extra bit of the closure is stored someplace that will outlive the function. There are several ways to have a closure escape its containing function:
Asynchronous execution: If you execute the closure asynchronously on a dispatch queue, the queue will hold onto the closure for you. You have no idea when the closure will be executed and there’s no guarantee it will complete before the function returns.
Storage: Storing the closure to a global variable, property, or any other bit of storage that lives on past the function call means the closure has also escaped.
for more details.
## 3- Explain [weak self] and [unowned self] ?
unowned ( non-strong reference ) does the same as weak with one exception: The variable will not become nil and must not be optional.
When you try to access the variable after its instance has been deallocated. That means, you should only use unowned when you are sure, that this variable will never be accessed after the corresponding instance has been deallocated.
However, if you don’t want the variable to be weak AND you are sure that it can’t be accessed after the corresponding instance has been deallocated, you can use unowned.
Every time used with non-optional types
Every time used with let
By declaring it [weak self] you get to handle the case that it might be nil inside the closure at some point and therefore the variable must be an optional. A case for using [weak self] in an asynchronous network request, is in a view controller where that request is used to populate the view.
## 4- What is ARC ?
ARC is a compile time feature that is Apple’s version of automated memory management. It stands for Automatic Reference Counting. This means that it only frees up memory for objects when there are zero strong references/ to them.
## 5- Explain #keyPath() ?
Using #keyPath(), a static type check will be performed by virtue of the key-path literal string being used as a StaticString or StringLiteralConvertible. At this point, it’s then checked to ensure that it
A) is actually a thing that exists and
B) is properly exposed to Objective-C.
## 6- What is iOS 11 SDK Features for Developers?
New MapKit Markers
Configurable File Headers
Block Based UITableView Updates
MapKit Clustering
Closure Based KVO
Vector UIImage Support
New MapKit Display Type
Named colors in Asset Catalog
Password Autofill
Face landmarks, Barcode and Text Detection
Multitasking using the new floating Dock, slide-over apps, pinned apps, and the new App Switcher
Location Permission: A flashing blue status bar anytime an app is collecting your location data in the background. Updated locations permissions that always give the user the ability to choose only to share location while using the app.
for more information.
## 7- What makes React Native special for iOS?
(Unlike PhoneGap) with React Native your application logic is written and runs in JavaScript, whereas your application UI is fully native; therefore you have none of the compromises typically associated with HTML5 UI.
Additionally (unlike Titanium), React introduces a novel, radical and highly functional approach to constructing user interfaces. In brief, the application UI is simply expressed as a function of the current application state.
## 8- What is NSFetchRequest?
NSFetchRequest is the class responsible for fetching from Core Data. Fetch requests are both powerful and flexible. You can use fetch requests to fetch a set of objects meeting the provided criteria, individual values and more.
## 9- Explain NSPersistentContainer
The persistent container creates and returns a container, having loaded the store for the application to it. This property is optional since there are legitimate error conditions that could cause the creation of the store to fail.
## 10- Explain NSFetchedResultsController
NSFetchedResultsController is a controller, but it’s not a view controller. It has no user interface. Its purpose is to make developers’ lives easier by abstracting away much of the code needed to synchronize a table view with a data source backed by Core Data.
Set up an NSFetchedResultsController correctly, and your table will mimic its data source without you have to write more than a few lines of code.
## 11- What is the three major debugging improvements in Xcode 8?
The View Debugger lets us visualize our layouts and see constraint definitions at runtime. Although this has been around since Xcode 6, Xcode 8 introduces some handy new warnings for constraint conflicts and other great convenience features.
The Thread Sanitizer is an all new runtime tool in Xcode 8 that alerts you to threading issues — most notably, potential race conditions.
The Memory Graph Debugger is also brand new to Xcode 8. It provides visualization of your app’s memory graph at a point in time and flags leaks in the Issue navigator.
## 12- What is the Test Driven Development of three simple rules?
You are not allowed to write any production code unless it is to make a failing unit test pass.
You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
You are not allowed to write any more production code than is sufficient to pass the one failing unit test.
## 13- Please explain final keyword into the class?
By adding the keyword final in front of the method name, we prevent the method from being overridden. If we can replace the final class keyword with a single word static and get the same behavior.
## 14- What does Yak Shaving mean?
Yak shaving is a programming term that refers to a series of tasks that need to be performed before a project can progress to its next milestone.
## 15- What is the difference open & public access level?
open allows other modules to use the class and inherit the class; for members, it allows others modules to use the member and override it. For more information,
I recommend reading the Swift language guide chapter on access control.
public only allows other modules to use the public classes and the public members. Public classes can no longer be subclassed, nor public members can be overridden.
## 16- What is the difference fileprivate, private and public private(set) access level ?
fileprivate is accessible within the current file, private is accessible within the current declaration.
public private(set) means getter is public, but the setter is private.
## 17- What is Internal access ?
Internal access enables entities to be used within any source file from their defining module, but not in any source file outside of the module.
Internal access is the default level of access. So even though we haven’t been writing any access control specifiers in our code, our code has been at an internal level by default.
## 18- What is the difference between BDD and TDD?
The main difference between BDD and TDD is the fact that BDD test cases can be read by non-engineers, which can be very useful in teams.
iOS I prefer Quick BDD framework and its “matcher framework,” called Nimble.
## 19- Please explain “Arrange-Act-Assert”
AAA is a pattern for arranging and formatting code in Unit Tests. If we were to write XCTests each of our tests would group these functional sections, separated by blank lines:
Arrange all necessary preconditions and inputs.
Act on the object or method under test.
Assert that the expected results have occurred.
## 20- What is the benefit of writing tests in iOS apps?
Writing tests first gives us a clear perspective on the API design, by getting into the mindset of being a client of the API before it exists.
Good tests serve as great documentation of expected behavior.
It gives us confidence to constantly refactor our code because we know that if we break anything our tests fail.
If tests are hard to write its usually a sign architecture could be improved. Following RGR ( Red — Green — Refactor ) helps you make improvements early on.
## 21- What is five essential practical guidelines to improve your typographic quality of mobile product designs?
1. Start by choosing your body text typeface.
2. Try to avoid mixing typefaces.
3. Watch your line length.
4. Balance line height and point size.
5. Use proper Apostrophes and Dashes.
## 22- Explain Forced Unwrapping
When we defined a variable as optional, then to get the value from this variable, we will have to unwrap it. This just means putting an exclamation mark at the end of the variable. The example of the implicitly unwrapped optional type is the IBOutlets we created for your view controller.
We have to use Forced Unwrapping when we know an optional has a value.
## 23- How to educate app with Context?
Education in context technique helping users interact with an element or surface in a way they have not done so previously. This technique often includes slight visual cues and subtle animation.

## 24- What is bitcode ?
Bitcode refers to to the type of code: “LLVM Bitcode” that is sent to iTunes Connect. This allows Apple to use certain calculations to re-optimize apps further (e.g: possibly downsize executable sizes). If Apple needs to alter your executable then they can do this without a new build being uploaded.
## 25- Explain Swift Standard Library Protocol ?
There are a few different protocol. Equatable protocol, that governs how we can distinguish between two instances of the same type. That means we can analyze. If we have a specific value is in our array. The comparable protocol, to compare two instances of the same type and sequence protocol: prefix(while:) and drop(while:) [SE-0045].
Swift 4 introduces a new Codable protocol that lets us serialize and deserialize custom data types without writing any special code.
## 26- What is the difference SVN and Git ?
SVN relies on a centralised system for version management. It’s a central repository where working copies are generated and a network connection is required for access.
Git relies on a distributed system for version management. You will have a local repository on which you can work, with a network connection only required to synchronise.
## 27- What is the difference CollectionViews & TableViews?
TableViews display a list of items, in a single column, a vertical fashion, and limited to vertical or horizontal scrolling only.
CollectionViews also display a list of items, however, they can have multiple columns and rows.
## 28- What is Alamofire doing?
Alamofire uses URL Loading System in the background, so it does integrate well with the Apple-provided mechanisms for all the network development. This means, It provides chainable request/response methods, JSON parameter and response serialization, authentication, and many other features. It has thread mechanics and executes requests on a background thread and call completion blocks on the main thread.
## 29- REST, HTTP, JSON — What’s that?
HTTP is the application protocol or set of rules, websites use to transfer data from the web server to client. The client (your web browser or app) use to indicate the desired action:
GET: Used to retrieve data, such as a web page, but doesn’t alter any data on the server.
HEAD: Identical to GET but only sends back the headers and none of the actual data.
POST: Used to send data to the server, commonly used when filling a form and clicking submit.
PUT: Used to send data to the specific location provided.
DELETE: Deletes data from the specific location provided.
REST, or REpresentational State Transfer, is a set of rules for designing consistent, easy-to-use and maintainable web APIs.
JSON stands for JavaScript Object Notation; it provides a straightforward, human-readable and portable mechanism for transporting data between two systems. Apple supplies the JSONSerialization class to help convert your objects in memory to JSON and vice-versa.
## 30- What problems does delegation solve?
Avoiding tight coupling of objects
Modifying behavior and appearance without the need to subclass objects
Allowing tasks to be handed off to any arbitrary object
## 31- What is the major purposes of Frameworks?
Frameworks have three major purposes:
Code encapsulation
Code modularity
Code reuse
You can share your framework with your other apps, team members, or the iOS community. When combined with Swift’s access control, frameworks help define strong, testable interfaces between code modules.
## 32- Explain Swift Package Manager
The Swift Package Manager will help to vastly improve the Swift ecosystem, making Swift much easier to use and deploy on platforms without Xcode such as Linux. The Swift Package Manager also addresses the problem of dependency hell that can happen when using many interdependent libraries.
The Swift Package Manager only supports using the master branch. Swift Package Manager now supports packages with Swift, C, C++ and Objective-C.
## 33- What is the difference between a delegate and an NSNotification?
Delegates and NSNotifications can be used to accomplish nearly the same functionality. However, delegates are one-to-one while NSNotifications are one-to-many.
## 34- Explain SiriKit Limitations
SiriKit cannot use all app types
Not a substitute for a full app only an extension
Siri requires a consistent Internet connection to work
Siri service needs to communicate Apple Servers.
## 35- Why do we use a delegate pattern to be notified of the text field’s events?
Because at most only a single object needs to know about the event.
## 36- How is an inout parameter different from a regular parameter?
A Inout passes by reference while a regular parameter passes by value.
## 37- Explain View Controller Lifecycle events order?
There are a few different lifecycle events
## - loadView
Creates the view that the controller manages. It’s only called when the view controller is created and only when done programatically. It is responsible for making the view property exist in the first place.
## - viewDidLoad
Called after the controller’s view is loaded into memory. It’s only called when the view is created.
## - viewWillAppear
It’s called whenever the view is presented on the screen. In this step the view has bounds defined but the orientation is not applied.
## - viewWillLayoutSubviews
Called to notify the view controller that its view is about to layout its subviews. This method is called every time the frame changes
## - viewDidLayoutSubviews
Called to notify the view controller that its view has just laid out its subviews. Make additional changes here after the view lays out its subviews.
## - viewDidAppear
Notifies the view controller that its view was added to a view hierarchy.
## - viewWillDisappear
Before the transition to the next view controller happens and the origin view controller gets removed from screen, this method gets called.
## - viewDidDisappear
After a view controller gets removed from the screen, this method gets called. You usually override this method to stop tasks that are should not run while a view controller is not on screen.
## - viewWillTransition(to:with:)
When the interface orientation changes, UIKit calls this method on the window’s root view controller before the size changes are about to be made. The root view controller then notifies its child view controllers, propagating the message throughout the view controller hierarchy.

## 38- What is the difference between LLVM and Clang?
Clang is the front end of LLVM tool chain ( “clang” C Language Family Frontend for LLVM ). Every Compiler has three parts .
1. Front end ( lexical analysis, parsing )
2. Optimizer ( Optimizing abstract syntax tree )
3. Back end ( machine code generation )
Front end ( Clang ) takes the source code and generates abstract syntax tree ( LLVM IR ).
## 39- What is Class ?
A class is meant to define an object and how it works. In this way, a class is like a blueprint of an object.
## 40- What is Object?
An object is an instance of a class.
## 41- What is interface?
The @interface in Objective-C has nothing to do with Java interfaces. It simply declares a public interface of a class, its public API.
## 42- When and why do we use an object as opposed to a struct?
Structs are value types. Classes(Objects) are reference types.
## 43- What is UIStackView?
UIStackView provides a way to layout a series of views horizontally or vertically. We can define how the contained views adjust themselves to the available space. Don’t miss this article.
## 44- What are the states of an iOS App?
Non-running — The app is not running.
Inactive — The app is running in the foreground, but not receiving events. An iOS app can be placed into an inactive state, for example, when a call or SMS message is received.
Active — The app is running in the foreground, and receiving events.
Background — The app is running in the background, and executing code.
Suspended — The app is in the background, but no code is being executed.
## 45- What are the most important application delegate methods a developer should handle?
The operating system calls specific methods within the application delegate to facilitate transitioning to and from various states. The seven most important application delegate methods a developer should handle are:
application:willFinishLaunchingWithOptions
Method called when the launch process is initiated. This is the first opportunity to execute any code within the app.
application:didFinishLaunchingWithOptions
Method called when the launch process is nearly complete. Since this method is called is before any of the app’s windows are displayed, it is the last opportunity to prepare the interface and make any final adjustments.
applicationDidBecomeActive
Once the application has become active, the application delegate will receive a callback notification message via the method applicationDidBecomeActive.
This method is also called each time the app returns to an active state from a previous switch to inactive from a resulting phone call or SMS.
applicationWillResignActive
There are several conditions that will spawn the applicationWillResignActive method. Each time a temporary event, such as a phone call, happens this method gets called. It is also important to note that “quitting” an iOS app does not terminate the processes, but rather moves the app to the background.
applicationDidEnterBackground
This method is called when an iOS app is running, but no longer in the foreground. In other words, the user interface is not currently being displayed. According to Apple’s UIApplicationDelegate Protocol Reference, the app has approximately five seconds to perform tasks and return. If the method does not return within five seconds, the application is terminated.
applicationWillEnterForeground
This method is called as an app is preparing to move from the background to the foreground. The app, however, is not moved into an active state without the applicationDidBecomeActive method being called. This method gives a developer the opportunity to re-establish the settings of the previous running state before the app becomes active.
applicationWillTerminate
This method notifies your application delegate when a termination event has been triggered. Hitting the home button no longer quits the application. Force quitting the iOS app, or shutting down the device triggers the applicationWillTerminate method. This is an opportunity to save the application configuration, settings, and user preferences.
## 46- What is the difference between property and instance variable?
A property is a more abstract concept. An instance variable is literally just a storage slot, as a slot in a struct. Normally other objects are never supposed to access them directly. Usually, a property will return or set an instance variable, but it could use data from several or none at all.
## 47- How can we add UIKit for Swift Package Manager?
Swift Package Manager is not supporting UIKit. We can create File Template or Framework for other projects.
## 48- Explain the difference between SDK and Framework
SDK is a set of software development tools. This set is used for the creation of applications. A framework is basically a platform which is used for developing software applications. It provides the necessary foundation on which the programs can be developed for a specific platform. SDK and Framework complement each other, and SDKs are available for frameworks.
## 49- What is Downcasting?
When we’re casting an object to another type in Objective-C, it’s pretty simple since there’s only one way to do it. In Swift, though, there are two ways to cast — one that’s safe and one that’s not.
as used for upcasting and type casting to bridged type
as? used for safe casting, return nil if failed
as! used to force casting, crash if failed. should only be used when we know the downcast will succeed.
## 50- Explain Labeled Statements
Using a labeled statement, we can specify which control structure we want to break no matter how deeply you nest our loops. This also works with continue. If we have a complex structure that contains nested for loops, a labeled statement will allow us to break from an outer loop and continue on with the execution of the method.