'''

@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class RecipeRequestDTO {
    private String name;
    private List<String> ingredients;
    private List<String> type;
    private String nationality;
    private String source;
//    private List<String> steps;
    private int portion;
    private String creator;
    private String cookTime;
    private List<String> imageLinks;
    private List<SectionRequestDTO> sectionRequestDTOs;
}

@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class RecipeResponseDTO {
    private String recipeId;
    private String name;
    private List<String> ingredients;
    private List<String> type;
    private String nationality;
    private String source;
    private List<RecipeSection> sections;
    private int portion;
    private String creator;
    private String cookTime;
    private List<String> imageLinks;
//    private Timestamp dateCreated;
}

@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class SectionRequestDTO {
    private String name;
    private List<String> steps;
    private String time;
    private int order;
}

'''