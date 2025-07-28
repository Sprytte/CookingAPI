'''
public class RecipeServiceImpl implements RecipeService{
    private final RecipeRepository recipeRepository;
    private final RecipeSectionRepository recipeSectionRepository;
    private final RecipeRequestMapper recipeRequestMapper;
    private final SectionRequestMapper sectionRequestMapper;

    @Override
    public List<RecipeResponseDTO> getRecipes(Map<String, String> queryParams) {
        String orderParameter = queryParams.get("order");
        String nationality = queryParams.get("nation");
        //name and date created (order)
        //type, nationality, author

//        if(nationality != null)
//            return recipeRepository.findAllByNationality(nationality);
        List<Recipe> recipes = recipeRepository.findAll();
        List<RecipeResponseDTO> recipeDTOs = new ArrayList<>();
        for(Recipe recipe: recipes){
            RecipeResponseDTO dto = new RecipeResponseDTO();
            List<RecipeSection> temp = new ArrayList<>();
            dto.setRecipeId(recipe.getRecipeId());
            dto.setName(recipe.getName());
            dto.setIngredients(recipe.getIngredients());
            dto.setType(recipe.getType());
            dto.setNationality(recipe.getNationality());
            dto.setSource(recipe.getSource());
            for(String sectionId: recipe.getSections()){
                temp.add(recipeSectionRepository.findById(Integer.parseInt(sectionId)));
            }
            dto.setSections(temp);
            dto.setPortion(recipe.getPortion());
            dto.setCreator(recipe.getCreator());
            dto.setCookTime(recipe.getCookTime());
            dto.setImageLinks(recipe.getImageLinks());
            recipeDTOs.add(dto);
        }

        return recipeDTOs;
    }

    @Override
    public RecipeResponseDTO getRecipe(String id) {
        Recipe recipe = recipeRepository.findByRecipeId(id);
        RecipeResponseDTO dto = new RecipeResponseDTO();
        List<RecipeSection> temp = new ArrayList<>();
        dto.setRecipeId(recipe.getRecipeId());
        dto.setName(recipe.getName());
        dto.setIngredients(recipe.getIngredients());
        dto.setType(recipe.getType());
        dto.setNationality(recipe.getNationality());
        dto.setSource(recipe.getSource());
        for(String sectionId: recipe.getSections()){
            temp.add(recipeSectionRepository.findById(Integer.parseInt(sectionId)));
        }
        dto.setSections(temp);
        dto.setPortion(recipe.getPortion());
        dto.setCreator(recipe.getCreator());
        dto.setCookTime(recipe.getCookTime());
        dto.setImageLinks(recipe.getImageLinks());

        return dto;
    }

    @Override
    public Recipe getRandomRecipe() {
        Random ran = new Random();
        int index = ran.nextInt((int)recipeRepository.count());

        return recipeRepository.findById(index).orElseThrow();
    }

    @Override
    public Recipe addRecipe(RecipeRequestDTO recipeRequestDTO, List<SectionRequestDTO> sectionRequestDTO) {
        Recipe recipe = recipeRequestMapper.requestModelToEntity(recipeRequestDTO);
        recipe.setRecipeId(UUID.randomUUID().toString());
        recipe.setDateCreated(Timestamp.valueOf(LocalDateTime.now()));

        List<String> sectionIds = returnSavedSections(sectionRequestDTO);

        recipe.setSections(sectionIds);

        recipeRepository.save(recipe);
        return recipe;
    }

    @Override
    public Recipe updateRecipe(String id, RecipeRequestDTO recipeRequestDTO, List<SectionRequestDTO> sectionRequestDTOS) {
        Recipe recipe = recipeRepository.findByRecipeId(id);
        BeanUtils.copyProperties(recipeRequestDTO, recipe); //This might fuck up for List types we'll see

        List<String> sectionIds = returnSavedSections(sectionRequestDTOS);

        recipe.setSections(sectionIds);

        recipeRepository.save(recipe);
        return recipe;
    }

    @Override
    public void deleteRecipe(String id) {
        recipeRepository.delete(recipeRepository.findByRecipeId(id));
    }

    private List<String> returnSavedSections(List<SectionRequestDTO> sectionRequestDTOList){
        List<String> sectionIds = new ArrayList<>();
        for(SectionRequestDTO sec : sectionRequestDTOList){
            RecipeSection section = recipeSectionRepository.save(sectionRequestMapper.requestModelToEntity(sec));
            sectionIds.add("" + section.getId());
        }

        return sectionIds;
    }
}
'''
#method to convert model to dto & vice versa